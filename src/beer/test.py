from django.test import TestCase
from turbobus.injection import inject

# from src.beer.axioma.entities.beer import Beer
# from src.beer.axioma.entities.friend import Friend
from src.beer.axioma.entities.order import Order
from src.beer.axioma.repositories import BeerRepository, FriendRepository, OrderRepository
from src.beer.capabilities.add_order_item import AddOrderItemCommand, AddOrderItemHandler



class OrderTestCase(TestCase):

    def test_adds_new_order_item_to_existing_pending_order(self):
        # Mock dependencies
        friend_repository_mock = inject(FriendRepository)
        beer_repository_mock = inject(BeerRepository)
        order_repository_mock = inject(OrderRepository)

        # Create test data
        friend_id = 1
        beer_id = 1
        quantity = 1

        # Create an existing pending order
        existing_order = Order(items=[])

        # Create an instance of the class under test
        handler = AddOrderItemHandler(
            order_repository=order_repository_mock,
            friend_repository=friend_repository_mock,
            beer_repository=beer_repository_mock
        )

        # Call the method under test
        command = AddOrderItemCommand(friend_id=friend_id, beer_id=beer_id, quantity=quantity)
        handler.execute(command)


        order = order_repository_mock.get_pending_order()

        assert order is not None
        
        assert len(order.items) == 1
        assert order.items[0].friend.id == friend_id
        assert order.items[0].beer.id == beer_id
        assert order.items[0].quantity == quantity
