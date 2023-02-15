from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    phone = models.CharField(max_length=12, unique=True)
    role = models.CharField(max_length=12)
    owner = models.ForeignKey(
        'users.User', null=True,
        on_delete=models.SET_NULL)


class Admin(User):
    pass


class Manager(User):
    pass


class CallCenter(User):
    pass
