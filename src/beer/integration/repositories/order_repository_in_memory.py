from src.beer.axioma.entities import Order
from src.beer.axioma.repositories import OrderRepository
from src.beer.axioma.utils import parse_id
from turbobus.injection import injectable_of


@injectable_of(OrderRepository)
class OrderRepositoryInMemory(OrderRepository):

    __paid_orders: dict[str, Order] = {}
    __pending_order: Order | None = None

    def save(self, order: Order) -> None:

        if order.is_paid:
            self.__paid_orders[parse_id(order.id)] = order
            self.__pending_order = None
            return

        self.__pending_order = order

    def get_pending_order(self) -> Order | None:
        return self.__pending_order
    
    def get_paid_orders(self) -> list[Order]:
        return list(self.__paid_orders.values())
