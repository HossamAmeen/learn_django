from django.db import models
from django_extensions.db.models import TimeStampedModel
from orders.models import Order

from users.models import User

class OrderTracking(TimeStampedModel):
    order =models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices=Order.OrderStatus.choices,
                              default=Order.OrderStatus.NEW)
    created_by = models.ForeignKey(User, null=True,
                                   on_delete=models.SET_NULL)
    comment = models.CharField(max_length=220)
