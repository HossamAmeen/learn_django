from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from orders.helpers import (create_client, create_trader, generate_order_code,
                            get_user_id_from_token)
from orders.models import Order
from orders.serializers import ListOrderSerializer, OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer

    def get_serializer_class(self, **kwargs):
        print(self.request.query_params.get('limit', False))
        # paginator = None
        if self.action in ['list', 'retrieve']:
            return ListOrderSerializer
        else:
            return OrderSerializer

    def create(self, request, *args, **kwargs):
        request.data['created_by'] = get_user_id_from_token(request)
        request.data['code'] = generate_order_code()
        if request.data.get('client') is None:
            if request.data.get('is_trader'):
                request.data['client'] = create_client(request.data)
            else:
                request.data['client'] = create_trader(request.data)
        # request.data['created_by'] = 1
        serializer_data = self.serializer_class(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        serializer_data.save()

        return Response(serializer_data.data, status=status.HTTP_200_OK)

    def updates(self, request, *args, **kwargs):
        pass

        


class DeliveryOrderViewSet(ModelViewSet):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer

    def get_serializer_class(self, **kwargs):
        print(self.request.query_params.get('limit', False))
        # paginator = None
        if self.action in ['list', 'retrieve']:
            return ListOrderSerializer
