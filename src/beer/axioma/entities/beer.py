from dataclasses import dataclass, field
from src.beer.axioma.utils import get_unique_integer_id


@dataclass(kw_only=True)
class Beer:
    id: int = field(default_factory=get_unique_integer_id)
    name: str
    price: float