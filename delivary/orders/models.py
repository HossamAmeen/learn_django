from django.db import models
from django_extensions.db.models import TimeStampedModel
from softdelete.models import SoftDeleteObject

from users.models import Customer, Delivery


class Order(TimeStampedModel, SoftDeleteObject):

    class OrderStatus(models.TextChoices):
        NEW = "new"
        DELIVERYASSIGNED = "assigned_to_delivery"
        INPROGRESS = "in_progress"
        OUTFORDELIVERY = "out_for_delivery"
        DELIVERED = "delivered"
        CANCELLED = "cancelled"

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.SET_NULL,
                                 null=True)
    address_from = models.TextField()
    address_to = models.TextField()
    order_code = models.CharField(unique=True, db_index=True, max_length=20)
    status = models.CharField(max_length=20, choices=OrderStatus.choices,
                              default=OrderStatus.NEW)
    city = models.CharField(max_length=20, null=True)


class Comment(TimeStampedModel, SoftDeleteObject):
    comment = models.CharField(max_length=150)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)