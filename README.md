# Getting Started

## Frontend

Para visualizar el frontend ejecuta:

```yarn install```

```yarn dev```

Y visita: http://localhost:5174/

## Instalación con docker

El proyecto está utilizando docker para configurar rápidamente el entorno en tu máquina. Por lo tanto, necesitas tener docker + docker-compose instalados. Si estás usando un sistema similar a UNIX, simplemente ejecuta los siguientes comandos en tu máquina.

```
make up
```
Este comando es similar a ejecutar docker-compose up -d. Y va a instalar la imagen de docker y las dependencias del proyecto en el contenedor. Entonces podrás ver el proyecto en tu http://localhost:9000

```
make shell
```

Nota: Si estás usando Windows y tienes docker instalado. Puedes ejecutar los comandos anteriores solo si tienes el paquete **make** instalado. Puedes instalarlo ejecutando:

```
choco install make
```

De lo contrario, necesitarás ejecutar los comandos en modo "feo", para lograr el mismo resultado:

```
docker-compose up -d
```
## Instalación manual
Si no eres fanático de docker. Entonces puedes instalar el proyecto usando poetry (Administrador de paquetes de Python). Solo sigue la [﻿Offical documentation.](https://python-poetry.org/docs/)﻿.

Una vez que tengas poetry instalado en tu máquina, simplemente ejecuta los siguientes comandos:

```
poetry install
```

```
poetry run python manage.py 0.0.0.0:9000
```

## Run
Una vez que tengas el servidor en funcionamiento, puedes interactuar con los siguientes endpoints:

`[GET | POST] api/v1/beers/'`: `name` y `price` son requeridos para crear una nueva cerveza

`[GET] api/v1/orders/calculate-total/`

`[POST] api/v1/orders/pay/`: envia `is_individual` en el payload de la request para indicar si la cuenta se pagara de manera individual o de manera compartida

`[POST] api/v1/orders/`: para agregar un nuevo elemento a la orden, envia `beer_id`, `friend_id`, `quantity` en el payload del request

# Development Guidelines
Para seguir las mejores prácticas. El proyecto está utilizando el Patrón de Diseño de Domain Driven Design + Patrón de Command Responsibility Segregation, que son excelentes para garantizar los principios de SOLID. Puedes seguir la imagen a continuación para entender la arquitectura del proyecto.

![ddd-layers.png](https://eraser.imgix.net/workspaces/EtmPQnoTnRa2bflkvGpd/sryDWTtHe6fe5632Wc8QLjPd2lU2/hPcZW8osOsh9F5Cj6UcQC.png?ixlib=js-3.7.0 "ddd-layers.png")

## Project Structure
- **Context**: you can see this folder as the core or main module of the current project. Inside this module you will find the next structure:
```
context/
├── axiom/
│   ├── entities/
│   ├── repositories/
│   ├── services/
│   └── value_objects/
├── capabilities/
└── integration/
    ├── repositories/
```
**Axiom layer**: en esta capa, vamos a colocar todos los conceptos comerciales como código Python. Tales como interfaces principales, objetos de valor, agregados, tipos.

**Capabilities layer**: Aquí, tendremos todas las acciones o casos de uso que un módulo es capaz de realizar.

**Integration layer**: probablemente necesites llamar a algunos servicios de terceros desde tus capabilities, pero no deberíamos incluir estas implementaciones en nuestra capa Axioma o Capabilities. En su lugar, usaremos la capa de integration para implementar estos servicios.

---

