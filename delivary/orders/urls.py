from django.urls import path
from orders.api import DeliveryOrderAPIView, OrderViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('orders/', OrderViewSet.as_view(
                                            {
                                                'get': 'list',
                                                "post": "create"
                                            }
                                        )),
    path('delivery/orders/', DeliveryOrderAPIView.as_view())
]
