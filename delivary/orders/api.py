from orders.helpers import (create_customer, create_trader,
                            generate_order_code, get_user_id_from_token)
from orders.models import Order
from orders.serializers import OrderSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        request.data[''] = get_user_id_from_token(request)
        request.data['code'] = generate_order_code()
        if request.data.get('customer') is None:
            if request.data.get('is_trader'):
                request.data['customer'] = create_customer(request.data)
            else:
                request.data['customer'] = create_trader(request.data)
        serializer_data = self.serializer_class(data=request.data)
        serializer_data.is_valid(raise_exception=True)
        serializer_data.save()

        return Response(serializer_data.data, status=status.HTTP_200_OK)


class DeliveryOrderAPIView(APIView):

    def get(self, request, *args, **kwargs):
        orders = Order.objects.filter()
        serializer_data = OrderSerializer(data=orders)
        serializer_data.is_valid()
        return Response(serializer_data.data, status=status.HTTP_200_OK)
