FROM python:3.12-bullseye as builder

ARG UID=1000 \
    GID=1000

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_CREATE=false \
    VIRTUALENV=/home/app/.venv \
    PIP_DEFAULT_TIMEOUT=100 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN groupadd -g ${GID} appgroup && useradd -m -u ${UID} -g appgroup -s /bin/bash app
USER app
RUN python3 -m venv $VIRTUALENV

ENV PATH="$VIRTUALENV/bin:$PATH"

USER app
WORKDIR /home/app

COPY --chown=app:appgroup pyproject* ./

RUN python -m pip install poetry

RUN poetry self update && \
    poetry install --only=main --no-root && \
    pip uninstall poetry -y

FROM python:3.12-slim

ARG UID=1000 \
    GID=1000

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    POETRY_VIRTUALENVS_CREATE=false \
    VIRTUALENV=/home/app/.venv \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_DEFAULT_TIMEOUT=100

RUN apt-get update && apt-get install make libpq-dev python3-dev -y && rm -rf /var/lib/apt/lists/*


RUN groupadd -g ${GID} appgroup && useradd -m -u ${UID} -g appgroup -s /bin/bash app
RUN mkdir -p /home/app/app /home/app/app/static_files /home/app/app/media_files && \
    chown -R app:appgroup /home/app/app /home/app/app/static_files /home/app/app/media_files

COPY --chown=app:appgroup --from=builder $VIRTUALENV $VIRTUALENV
ENV PATH="$VIRTUALENV/bin:$PATH"

WORKDIR /home/app/app
USER app

COPY --chown=app:appgroup . .

CMD python manage.py runserver 0.0.0.0:9000
