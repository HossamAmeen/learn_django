from django.urls import path
from orders.api import DeliveryOrderViewSet, OrderViewSet

urlpatterns = [
    path('orders/', OrderViewSet.as_view(
                                            {
                                                'get': 'list',
                                                "post": "create"
                                            }
                                        )),
    path('orders/<int:pk>/', OrderViewSet.as_view(
                                            {
                                                'get': 'retrieve',
                                                "patch": "partial_update"
                                            }
                                        )),
    path('delivery/orders/', DeliveryOrderViewSet.as_view(
         {'get': 'list'})),
    path('delivery/orders/<int:pk>/', DeliveryOrderViewSet.as_view(
         {'get': 'retrieve'}))
]
