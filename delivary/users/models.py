from django.contrib.auth.models import AbstractUser
from django.db import models
from softdelete.models import SoftDeleteObject


class User(SoftDeleteObject, AbstractUser):
    phone = models.CharField(max_length=12, unique=True)
    role = models.CharField(max_length=12)
    created_by = models.ForeignKey(
        'users.User', null=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.role}: {self.first_name}"


class Admin(User):
    pass


class Manager(User):
    pass


class CallCenter(User):
    pass


class Delivery(User):
    national_id = models.CharField(max_length=12, unique=True)
    document_url = models.URLField(null=True)
    delivery_tool = models.CharField(max_length=20, null=True)
    vacation_day = models.CharField(max_length=12)
    company_percentage = models.IntegerField()
    guarantee_value = models.IntegerField(null=True)
    shift_start = models.TimeField()
    shift_end = models.TimeField()


class Customer(User):
    note = models.TextField(null=True)


class Trader(Customer):
    pass
