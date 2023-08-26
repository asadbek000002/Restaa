from django.contrib import admin
from .models import *
admin.site.register(Menu)
admin.site.register(CartItem)
admin.site.register(Cart)
import requests
from _decimal import Decimal


class ExchangeRateService:
    def get_exchange_rate(self, base_currency, target_currency):
        response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{base_currency}")
        data = response.json()
        exchange_rate = data['rates'].get(target_currency)
        return exchange_rate


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ['name', 'menu', 'porsiya', 'real_price', 'price', 'quantity', 'created', 'updated']




