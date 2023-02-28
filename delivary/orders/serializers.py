from users.serializers import ClientSerializer, DeliverySerializer, UserSerializer
from orders.models import Order
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"


class ListOrderSerializer(serializers.ModelSerializer):
    delivery = UserSerializer()
    client = UserSerializer()
    created_by = UserSerializer()

    class Meta:
        model = Order
        fields = "__all__"