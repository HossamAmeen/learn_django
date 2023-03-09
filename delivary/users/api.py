from django.contrib.auth.hashers import make_password
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.response import Response
from users.models import (Admin, CallCenter, Client, Delivery, Manager, Trader,
                          Vacation)
from users.serializers import (AdminSerializer, CallCenterSerializer,
                               ClientSerializer, DeliverySerializer, ListVacationSerializer,
                               ManagerSerializer, TraderSerializer,
                               VacationSerializer)


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
        super().perform_update(serializer)
        if serializer.validated_data.get('password'):
            serializer.save(password=make_password(
                serializer.validated_data['password']))

class ManagerViewSet(ModelViewSet):
    serializer_class = ManagerSerializer
    queryset = Manager.objects.filter()
    permission_classes = []
    # permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']),
            created_by_id=1)

    def perform_update(self, serializer):
        super().perform_update(serializer)
        if serializer.validated_data.get('password'):
            serializer.save(password=make_password(
                serializer.validated_data['password']))

class CallCenterViewSet(ModelViewSet):
    serializer_class = CallCenterSerializer
    queryset = CallCenter.objects.all()
    permission_classes = []
    # permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']),
            created_by_id=1)

    def perform_update(self, serializer):
        super().perform_update(serializer)
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
        super().perform_update(serializer)
        if serializer.validated_data.get('password'):
            serializer.save(password=make_password(
                serializer.validated_data['password']))


class ClientViewSet(ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = []
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['phone']
    # permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']),
            created_by_id=1)

    def perform_update(self, serializer):
        super().perform_update(serializer)
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
        super().perform_update(serializer)
        if serializer.validated_data.get('password'):
            serializer.save(password=make_password(
                serializer.validated_data['password']))


class VacationViewSet(ModelViewSet):
    queryset = Vacation.objects.all()
    serializer_class = VacationSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'post', 'patch', 'put']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'status', 'delivery', 'delivery__phone']

    def get_serializer_class(self, *args, **kwargs):
        if self.action in ['list', 'retrieve']:
            return ListVacationSerializer
        else:
            return VacationSerializer

    def get_queryset(self):
        token = AccessToken(self.request.META.get("HTTP_AUTHORIZATION")
                            .split(" ")[1])

        if token['role'] == "delivery":
            self.queryset = self.queryset.filter(created_by=token['user_id'])

        return self.queryset.order_by('-id')

    def create(self, request, *args, **kwargs):
        token = AccessToken(self.request.META.get("HTTP_AUTHORIZATION")
                            .split(" ")[1])

        if token['role'] == "delivery":
            request.data['delivery'] = token['user_id']

        request.data['created_by'] = token['user_id']
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
