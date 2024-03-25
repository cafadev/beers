from abc import ABC
from src.beer.axioma.entities import Beer, Order, Friend


class FriendRepository(ABC):

    def save(self, friend: Friend) -> None:
        ...

    def get_by_id(self, friend_id: int) -> Friend:
        ...

    def get_all(self) -> list[Friend]:
        ...

class BeerRepository(ABC):

    def save(self, beer: Beer) -> None:
        ...

    def get_by_id(self, beer_id: int) -> Beer:
        ...

    def get_all(self) -> list[Beer]:
        ...

class OrderRepository(ABC):

    def save(self, order: Order) -> None:
        ...

    def get_pending_order(self) -> Order | None:
        ...

    def get_paid_orders(self) -> list[Order]:
        ...
