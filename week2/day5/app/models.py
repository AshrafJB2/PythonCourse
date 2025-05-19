from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class MenuItems(models.Model):
    item_name = models.CharField(max_length=30, null=False)
    item_price = models.SmallIntegerField(default=0)


class Role(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    USER = 'user', 'User'


class TheUser(models.Model):
    username = models.CharField(max_length=30, null=False, unique=True)
    password = models.CharField(max_length=30, null=False)
    email = models.EmailField(null=False, unique=True)
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER,
    )
    def __str__(self):
        return self.username
    
    