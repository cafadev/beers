from dataclasses import dataclass

from src.beer.axioma.repositories import OrderRepository

@dataclass(kw_only=True)
class ProcessPaymentCommand:

    is_individual_payment: bool


@dataclass(kw_only=True)
class ProcessPaymentHandler:

    order_repository: OrderRepository

    def execute(self, command) -> None:
        order = self.order_repository.get_pending_order()

        if order is None:
            return
        
        order.is_paid = True
        order.is_individual_payment = command.is_individual_payment

        self.order_repository.save(order)
