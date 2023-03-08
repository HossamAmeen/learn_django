from rest_framework.viewsets import ModelViewSet
from basic.helpers import get_role_and_user_id
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from orders.models import Order
from tracking.serializers import OrderTrackSerializer
from .models import OrderTracking


class TrackingViewSet(ModelViewSet):
    queryset= OrderTracking.objects.all().order_by("-id")
    serializer_class = OrderTrackSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        _, request.data['created_by'] = get_role_and_user_id(request)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # # we will move it to signal or save model
        # order = Order.objects.filter(id=request.data['order']).first()
        # order.status = request.data['status']
        # order.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
