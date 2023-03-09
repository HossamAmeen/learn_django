import random
import re
from datetime import datetime

from rest_framework_simplejwt.tokens import AccessToken

from users.serializers import ClientSerializer, TraderSerializer



def get_user_id_from_token(request):
    if request.META.get("HTTP_AUTHORIZATION"):
        token = AccessToken(request.META.get("HTTP_AUTHORIZATION")
                            .split(" ")[1])
    else:
        return None
    return token['user_id']


def generate_order_code():
    # order code contain from current time with remove (-,'',:)
    # YearMonthDayHourMinuteSecond_5DigitsRandom
    return re.sub('[- :]', '', str(datetime.now()))[:14] + "_" + \
        str(random.randint(10000, 99999))


def create_client(request_data):

    request_data['created_by'] = 1
    request_data['password'] = "admin_123"
    request_data['role'] = 'client'
    request_data['username'] = request_data['phone']
    client_serializer = ClientSerializer(data=request_data)
    client_serializer.is_valid(raise_exception=True)
    client_serializer.save()
    return client_serializer.data['id']


def create_trader(request_data):
    request_data['created_by'] = 1
    request_data['password'] = "admin_123"
    request_data['role'] = 'trader'
    request_data['username'] = request_data['phone']
    client_serializer = TraderSerializer(data=request_data)
    client_serializer.is_valid(raise_exception=True)
    client_serializer.save()
    return client_serializer.data['id']
