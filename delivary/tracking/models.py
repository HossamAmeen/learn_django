from django.db import models
from django_extensions.db.models import TimeStampedModel
from users.models import Delivery
from orders.models import Order

from users.models import User

class OrderTracking(TimeStampedModel):
    
    order =models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=20, choices=Order.OrderStatus.choices,
                              default=Order.OrderStatus.NEW)
    created_by = models.ForeignKey(User, null=True,
                                   on_delete=models.SET_NULL)
    delivery = models.ForeignKey(Delivery, null=True, related_name="delivery",
                                 on_delete=models.SET_NULL)
    comment = models.CharField(max_length=220, null=True)

    def save(self, **kwargs):
        super().save(**kwargs)
        self.order.status = self.status
        self.order.save()
        return