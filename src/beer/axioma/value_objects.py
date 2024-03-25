from dataclasses import dataclass

from src.beer.axioma.entities.beer import Beer
from src.beer.axioma.entities.friend import Friend


@dataclass(kw_only=True)
class OrderItem:
    friend: Friend
    beer: Beer
    quantity: int