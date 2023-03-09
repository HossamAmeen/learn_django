from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated
from basic.helpers import get_role_and_user_id
from orders.constanct import ORDER_FILTER, ORDER_SEARCH
from tracking.models import OrderTracking
from orders.helpers import (create_client, create_trader, generate_order_code,
                            get_user_id_from_token)
from orders.models import Order
from orders.serializers import ListOrderSerializer, OrderSerializer, UpdateOrderSerializer
from rest_framework import filters

class OrderViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ORDER_FILTER
    search_fields = ORDER_SEARCH
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self, **kwargs):
        print(self.request.query_params.get('limit', False))
        # paginator = None
        if self.action in ['list', 'retrieve']:
            return ListOrderSerializer
        elif self.action in ['update', 'partial_update']:
            return UpdateOrderSerializer
        else:
            return OrderSerializer

    def create(self, request, *args, **kwargs):
        _, request.data['created_by'] = get_role_and_user_id(request)
        request.data['code'] = generate_order_code()
        if request.data.get('client') is None:
            if request.data.get('is_trader'):
                request.data['client'] = create_client(request.data)
            else:
                request.data['client'] = create_trader(request.data)
        request.data['created_by'] = 1
        serializer_data = self.serializer_class(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        serializer_data.save()

        return Response(serializer_data.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.data.get('status') == Order.OrderStatus.DELIVERED:
            OrderTracking.objects.create(
                order= instance, status=request.data['status']
            )
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
        

class DeliveryOrderViewSet(ModelViewSet):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ORDER_FILTER
    permission_classes = (IsAuthenticated,)
    search_fields = ORDER_SEARCH

    def get_serializer_class(self, **kwargs):
        # print(self.request.query_params.get('limit', False))
        # paginator = None
        if self.action in ['list', 'retrieve']:
            return ListOrderSerializer

    def get_queryset(self):
        _, user_id = get_role_and_user_id(self.request)
        self.queryset = self.queryset.filter(delivery=user_id)
        return self.queryset.order_by('-id')
