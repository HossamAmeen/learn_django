from django.urls import path
from orders.api import DeliveryOrderAPIView, OrderViewSet

urlpatterns = [
    path('orders/', OrderViewSet.as_view(
                                            {
                                                'get': 'list',
                                                "post": "create"
                                            }
                                        )),
    path('delivery/orders/', DeliveryOrderAPIView.as_view())
]
