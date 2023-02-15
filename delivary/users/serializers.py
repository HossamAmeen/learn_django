from django.contrib.auth.hashers import (make_password)
from rest_framework import serializers
from users.models import Admin


class AdminSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Admin
        exclude = ['last_login', 'is_superuser', 'is_staff',
                   'groups', 'user_permissions',
                   'date_joined', 'first_name', 'last_name']

    # def validate(self, attrs):
    #     if attrs.get('password'):
      
    #         if attrs.get('password_confirm') and \
    #             attrs['password'] != attrs['password_confirm']:
    #             raise serializers.ValidationError(
    #                 {"password": "Password fields didn't match."})

    #     return attrs
