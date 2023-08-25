from django.contrib import admin
from total.models import *
from decimal import Decimal


@admin.register(Total)
class TotalmAdmin(admin.ModelAdmin):
    list_display = ['name', 'total_order_price', 'total_quantity']
    
    
    
    def total_order_price(self,obj):
        total_sum = Decimal('0')
        order_items = OrderItem.objects.all()
        for order_item in order_items:
            total_sum += order_item.order_item_total_price
        return f"{total_sum:.2f}"

    
    def total_quantity(self, obj):
        t_quantity = Decimal('0')
        quantities = OrderItem.objects.all()
        for quantity in quantities:
            t_quantity += quantity.quantity
        return f"{t_quantity}"   
    
    
