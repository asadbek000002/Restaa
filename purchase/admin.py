from django.contrib import admin
from purchase.models import OrderItem
from _decimal import Decimal
import requests
# Register your models here.



# admin.site.register(OrderItem)
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'order_items', 'real_price_order', 'quantity', 'date_added']
    

    def order_items(self, obj):
            total = obj.meal.price * Decimal(obj.quantity)
            return total



    def real_price_order(self, obj):
            total = obj.meal.real_price * Decimal(obj.quantity)
            return total




    def name(self, obj):
            return obj.meal.name




