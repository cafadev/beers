from dataclasses import dataclass, field
from uuid import UUID, uuid4

from src.beer.axioma.value_objects import OrderItem


@dataclass(kw_only=True)
class Order:
    id: UUID = field(default_factory=uuid4, init=False)
    items: list[OrderItem]
    is_paid: bool = False
    is_individual_payment: bool = False

    def total_by_friend(self) -> dict[str, float]:
        amount_by_friend: dict[str, float] = {}

        if self.is_individual_payment:
            for order in self.items:
                amount_by_friend[order.friend.name] = amount_by_friend.get(str(order.friend.id), 0) + order.beer.price * order.quantity

        else: 
            total = sum([order.beer.price * order.quantity for order in self.items])
            amount_by_friend = {order.friend.name: total for order in self.items}

        return amount_by_friend
