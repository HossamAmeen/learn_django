from rest_framework import serializers

from users.constant import EXCLUDEFROMUSERMODEL
from users.models import (Admin, CallCenter, Customer, Delivery, Manager,
                          Trader, User)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'role', 'phone']


class AdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Admin
        exclude = EXCLUDEFROMUSERMODEL


class ManagerSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, required=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Manager
        exclude = EXCLUDEFROMUSERMODEL


class CallCenterSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, required=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = CallCenter
        exclude = EXCLUDEFROMUSERMODEL


class DeliverySerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, required=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Delivery
        exclude = EXCLUDEFROMUSERMODEL
        depth = 1


class CustomerSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, required=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Customer
        exclude = EXCLUDEFROMUSERMODEL


class TraderSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, required=True)
    created_by = serializers.StringRelatedField()

    class Meta:
        model = Trader
        exclude = EXCLUDEFROMUSERMODEL
