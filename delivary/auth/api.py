# from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView

from auth.serializers import MyTokenObtainPairSerializer, RegisterSerializer
from users.models import Delivery, User
from users.serializers import DeliverySerializer, UserSerializer


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class profileAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        token = AccessToken(request.META.get("HTTP_AUTHORIZATION")
                            .split(" ")[1])
        if token['role'] == "delivery":
            deliver = get_object_or_404(Delivery, id=token['user_id'])
            profile_data = DeliverySerializer(instance=deliver).data
        else:
            user = get_object_or_404(User, id=token['user_id'])
            profile_data = UserSerializer(instance=user).data

        return Response(profile_data)
