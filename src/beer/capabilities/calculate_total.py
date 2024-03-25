from dataclasses import dataclass
from src.beer.axioma.repositories import OrderRepository


@dataclass(kw_only=True)
class CalculateTotalCommand:

    is_individual_payment: bool = False

@dataclass(kw_only=True)
class CalculateTotalHandler:

    order_repository: OrderRepository

    def execute(self, command: CalculateTotalCommand) -> dict[str, float]:
        order = self.order_repository.get_pending_order()

        if order is None:
            return {}

        order.is_individual_payment = command.is_individual_payment
        return order.total_by_friend()
