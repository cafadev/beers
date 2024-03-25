from turbobus.injection import inject
from rest_framework import views

from rest_framework.response import Response
from rest_framework import status

from src.beer import BeerRepository, FriendRepository, OrderRepository
from src.beer.axioma.entities.beer import Beer
from src.beer.axioma.entities.friend import Friend
from src.beer.capabilities.add_order_item import AddOrderItemCommand, AddOrderItemHandler
from src.beer.capabilities.calculate_total import CalculateTotalCommand, CalculateTotalHandler
from src.beer.capabilities.process_payment import ProcessPaymentCommand, ProcessPaymentHandler
from src.beer.integration.serializers import BeerSerializer, FriendSerializer, OrderItemSerializer, OrderSerializer

beer_repository = inject(BeerRepository)
friend_repository = inject(FriendRepository)
order_repository = inject(OrderRepository)

add_order_item = AddOrderItemHandler(
    order_repository=order_repository,
    friend_repository=friend_repository,
    beer_repository=beer_repository
)
calculate_total = CalculateTotalHandler(
    order_repository=order_repository
)
process_payment = ProcessPaymentHandler(
    order_repository=order_repository
)


class BeerAPIView(views.APIView):

    serializer_class = BeerSerializer

    def get(self, request, format=None):
        beers = beer_repository.get_all()

        serializer = BeerSerializer(beers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BeerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        beer = Beer(**serializer.data)
        beer_repository.save(beer)

        serializer = BeerSerializer(beer)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class OrderAPIView(views.APIView):

    serializer_class = OrderSerializer

    def get(self, request):
        orders = order_repository.get_paid_orders()
        serializer = OrderSerializer(orders, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderItemSerializer(data=request.data, write_only=True)
        serializer.is_valid(raise_exception=True)

        add_order_item_command = AddOrderItemCommand(**request.data)
        order = add_order_item.execute(add_order_item_command)

        serializer = OrderSerializer(order)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

class OrderCalculateTotalAPIView(views.APIView):

    def get(self, request):
        calculate_total_command = CalculateTotalCommand(
            is_individual_payment=request.query_params.get('is_individual_payment', False)
        )
        total = calculate_total.execute(calculate_total_command)

        return Response(total, status=status.HTTP_200_OK)
    

class OrderPayAPIView(views.APIView):

    def post(self, request):
        process_payment_command = ProcessPaymentCommand(
            is_individual_payment=request.data.get('is_individual_payment', False)
        )
        process_payment.execute(process_payment_command)

        return Response(status=status.HTTP_202_ACCEPTED)
    

class FriendAPIView(views.APIView):

    def get(self, request):
        friends = friend_repository.get_all()

        serializer = FriendSerializer(friends, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = FriendSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        friend = Friend(**serializer.data)
        friend_repository.save(friend)

        serializer = FriendSerializer(friend)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
