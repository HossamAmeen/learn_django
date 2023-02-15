from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import AccessToken
from users.models import Admin
from users.serializers import AdminSerializer
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import (
    check_password,
    is_password_usable,
    make_password,
)


class AdminViewSet(ModelViewSet):
    serializer_class = AdminSerializer
    queryset = Admin.objects.all()
    permission_classes = []
    # permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']),
            owner_id=1)

    def perform_update(self, serializer):
        if serializer.validated_data.get('password'):
            serializer.save(password=make_password(
                serializer.validated_data['password']))
