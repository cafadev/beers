from django.urls import path
from typing import Any
from rest_framework.routers import DefaultRouter
from .views import BeerAPIView, OrderAPIView, OrderCalculateTotalAPIView, OrderPayAPIView, FriendAPIView

router = DefaultRouter()

urlpatterns: list[Any] = [
    path('beers/', BeerAPIView.as_view(), name='beer-list-create'),
    path('orders/calculate-total', OrderCalculateTotalAPIView.as_view(), name='order-calculate-total'),
    path('orders/pay', OrderPayAPIView.as_view(), name='order-pay'),
    path('orders/', OrderAPIView.as_view(), name='order-add-item'),
    path('friends/', FriendAPIView.as_view(), name='friend-list-create'),
] + router.urls
