from django.db import models

# Create your models here.

class MenuItems(models.Model):
    item_name = models.CharField(max_length=30, null=False)
    item_price = models.SmallIntegerField(default=0)