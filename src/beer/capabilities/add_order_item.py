from dataclasses import dataclass

from src.beer.axioma.entities.order import Order
from src.beer.axioma.repositories import BeerRepository, FriendRepository, OrderRepository
from src.beer.axioma.value_objects import OrderItem


@dataclass(kw_only=True)
class AddOrderItemCommand:

    friend_id: int
    beer_id: int
    quantity: int


@dataclass(kw_only=True)
class AddOrderItemHandler:

    order_repository: OrderRepository
    friend_repository: FriendRepository
    beer_repository: BeerRepository

    def execute(self, command: AddOrderItemCommand):
        friend = self.friend_repository.get_by_id(command.friend_id)
        beer = self.beer_repository.get_by_id(command.beer_id)

        order = self.order_repository.get_pending_order()

        if order is None:
            order = Order(items=[])

        order.items.append(OrderItem(friend=friend, beer=beer, quantity=command.quantity))
        self.order_repository.save(order)

        return order

