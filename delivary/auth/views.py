# from django.contrib.auth.models import User
from auth.serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.views import TokenObtainPairView
from users.models import User


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class profileAPIView(APIView):
    def get(self, request, format=None):
        token = AccessToken(request.META.get("HTTP_AUTHORIZATION").split(" ")[1])
        user_id = token['id']
        return Response({"test": "token"})
