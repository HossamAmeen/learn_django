from rest_framework import serializers

from orders.models import Order
from users.serializers import (ClientSerializer, DeliverySerializer,
                               UserSerializer)


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"


class ListOrderSerializer(serializers.ModelSerializer):
    delivery = DeliverySerializer()
    client = ClientSerializer()
    created_by = UserSerializer()

    class Meta:
        model = Order
        fields = "__all__"