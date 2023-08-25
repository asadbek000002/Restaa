from django.db import models
from purchase.models import OrderItem
# Create your models here.

class Total(models.Model):
    name = models.CharField(max_length=30)
    order_item = models.ForeignKey(OrderItem, on_delete=models.SET_NULL, null=True, blank=True)