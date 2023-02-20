from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import AccessToken

from users.models import Admin, CallCenter, Customer, Delivery, Manager, Trader
from users.serializers import (AdminSerializer, CallCenterSerializer,
                               CustomerSerializer, DeliverySerializer,
                               ManagerSerializer, TraderSerializer)


class AdminViewSet(ModelViewSet):
    serializer_class = AdminSerializer
    queryset = Admin.objects.all()
    permission_classes = []
    # permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']),
            created_by_id=1)

    def perform_update(self, serializer):
        if serializer.validated_data.get('password'):
            serializer.save(password=make_password(
                serializer.validated_data['password']))


class ManagerViewSet(ModelViewSet):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()
    permission_classes = []
    # permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']),
            created_by_id=1)

    def perform_update(self, serializer):
        if serializer.validated_data.get('password'):
            serializer.save(password=make_password(
                serializer.validated_data['password']))


class CAllCenterViewSet(ModelViewSet):
    serializer_class = CallCenterSerializer
    queryset = CallCenter.objects.all()
    permission_classes = []
    # permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']),
            created_by_id=1)

    def perform_update(self, serializer):
        if serializer.validated_data.get('password'):
            serializer.save(password=make_password(
                serializer.validated_data['password']))


class DeliveryViewSet(ModelViewSet):
    serializer_class = DeliverySerializer
    queryset = Delivery.objects.all()
    permission_classes = []
    # permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']),
            created_by_id=1)

    def perform_update(self, serializer):
        if serializer.validated_data.get('password'):
            serializer.save(password=make_password(
                serializer.validated_data['password']))


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = []
    # permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']),
            created_by_id=1)

    def perform_update(self, serializer):
        if serializer.validated_data.get('password'):
            serializer.save(password=make_password(
                serializer.validated_data['password']))


class TraderViewSet(ModelViewSet):
    serializer_class = TraderSerializer
    queryset = Trader.objects.all()
    permission_classes = []
    # permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']),
            created_by_id=1)

    def perform_update(self, serializer):
        if serializer.validated_data.get('password'):
            serializer.save(password=make_password(
                serializer.validated_data['password']))
