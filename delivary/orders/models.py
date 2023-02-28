from django.db import models
from django_extensions.db.models import TimeStampedModel
from softdelete.models import SoftDeleteObject
from users.models import Client, Delivery, User


class Order(TimeStampedModel, SoftDeleteObject):

    class OrderStatus(models.TextChoices):
        NEW = "new"
        DELIVERYASSIGNED = "assigned_to_delivery"
        INPROGRESS = "in_progress"
        OUTFORDELIVERY = "out_for_delivery"
        DELIVERED = "delivered"
        CANCELLED = "cancelled"

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.SET_NULL,
                                 null=True)
    address_source = models.TextField()
    address_destination = models.TextField()
    code = models.CharField(unique=True, db_index=True, max_length=20)
    status = models.CharField(max_length=20, choices=OrderStatus.choices,
                              default=OrderStatus.NEW)
    details = models.TextField()
    estimated_date = models.DateField(auto_now=True)
    estimated_time = models.TimeField(null=True)
    city = models.CharField(max_length=20, null=True)
    item_counter = models.IntegerField(default=1)
    created_by = models.ForeignKey(User, null=True, related_name="by",
                                   on_delete=models.SET_NULL)


class Comment(TimeStampedModel, SoftDeleteObject):
    comment = models.CharField(max_length=150)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
