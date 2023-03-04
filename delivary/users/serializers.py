from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.constant import EXCLUDEFROMUSERMODEL
from users.models import (Admin, CallCenter, Client, Delivery, Manager, Trader,
                          User, Vacation)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'role', 'phone']


class ListAdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Admin
        exclude = EXCLUDEFROMUSERMODEL
        depth = 1


class AdminSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Admin
        exclude = EXCLUDEFROMUSERMODEL
        depth = 1


class ManagerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Manager
        exclude = EXCLUDEFROMUSERMODEL
        depth = 1


class CallCenterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CallCenter
        exclude = EXCLUDEFROMUSERMODEL
        depth = 1


class DeliverySerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Delivery
        exclude = EXCLUDEFROMUSERMODEL
        depth = 1


class ClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Client
        exclude = EXCLUDEFROMUSERMODEL
        depth = 1

    def creates(self, validated_data):
        validated_data['username'] = validated_data['phone']
        validated_data['password'] = "admin_123"
        validated_data['role'] = 'client'
        validated_data['password'] = make_password("admin")
        super().create(validated_data)


class TraderSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Trader
        exclude = EXCLUDEFROMUSERMODEL
        depth = 1

    def creates(self, validated_data):
        validated_data['username'] = validated_data['phone']
        validated_data['password'] = "admin_123"
        validated_data['role'] = 'trader'
        validated_data['password'] = make_password("admin")
        super().create(validated_data)


class ListVacationSerializer(serializers.ModelSerializer):
    delivery = UserSerializer()
    created_by = UserSerializer()

    class Meta:
        model = Vacation
        fields = "__all__"


class VacationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacation
        fields = "__all__"