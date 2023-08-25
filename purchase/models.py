from django.db import models
from decimal import Decimal
from mainapp.models import Meal




class OrderItem(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.SET_NULL, related_name='order_items', blank=True, null=True)
    quantity = models.DecimalField(default=0, null=True, blank=True, max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            return self.meal.name

    @property
    def order_item_price(self):
            total = self.meal.price * Decimal(self.quantity)
            return total

    @property
    def order_item_total_price(self):
            total = self.meal.price * Decimal(self.quantity)
            return Decimal(total)


    @staticmethod
    def total_order_price():
        total_sum = Decimal('0')
        order_items = OrderItem.objects.all()
        for order_item in order_items:
            total_sum += order_item.order_item_total_price
        return f"{total_sum:.2f}"

    @staticmethod
    def total_quantity():
        t_quantity = Decimal('0')
        quantities = OrderItem.objects.all()
        for quantity in quantities:
            t_quantity += quantity.quantity
        return f"{t_quantity}"