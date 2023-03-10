from rest_framework import serializers

from users.serializers import UserSerializer
from .models import OrderTracking


class OrderTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderTracking
        fields = "__all__"

class ListOrderTrackingSerializer(serializers.ModelSerializer):
    created_by = UserSerializer()
    delivery = UserSerializer()

    class Meta:
        model = OrderTracking
        fields = "__all__"
