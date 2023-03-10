from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from softdelete.models import SoftDeleteObject


class User(AbstractUser):
    phone = models.CharField(max_length=12, unique=True)
    role = models.CharField(max_length=12)
    created_by = models.ForeignKey(
        'users.User', null=True,
        on_delete=models.SET_NULL)

    objects = UserManager()
    # objects = SoftDeleteManager()


class Admin(User):
    pass


class Manager(User):
    pass


class CallCenter(User):
    pass


class Delivery(User):
    national_id = models.CharField(max_length=14, unique=True)
    document_url = models.URLField(null=True)
    delivery_tool = models.CharField(max_length=20, null=True)
    vacation_day = models.CharField(max_length=12)
    company_percentage = models.IntegerField()
    guarantee_value = models.IntegerField(null=True)
    level_badge = models.CharField(max_length=50, null=True)
    custody_value = models.IntegerField(null=True)
    shift_start = models.TimeField()
    shift_end = models.TimeField()


class Client(User):
    note = models.TextField(null=True)
    address = models.TextField()
    address_2 = models.TextField(null=True, blank=True)


class Trader(Client):
    pass


class Vacation(models.Model):
    class StatusType(models.TextChoices):
        PENDING = "pending"
        ACCEPT = "accept"
        CANCEL = "cancel"

    delivery = models.ForeignKey(Delivery, related_name='vaction',
                                 related_query_name="vacations",
                                 on_delete=models.DO_NOTHING)
    date = models.DateField()
    reason = models.TextField(null=True)
    note = models.TextField(null=True)
    status = models.CharField(
        choices=StatusType.choices, default=StatusType.PENDING, max_length=20)
    created_by = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
