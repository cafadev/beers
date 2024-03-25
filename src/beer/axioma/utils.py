from typing import Any
from datetime import datetime


def parse_id(id: Any) -> str:
    return str(id)


def get_unique_integer_id() -> int:
    curr_dt = datetime.now()
    timestamp = int(round(curr_dt.timestamp()))
    
    return timestamp
