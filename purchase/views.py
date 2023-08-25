from django.shortcuts import render
from .models import *
# Create your views here.


def checkout(request):
    cart = OrderItem.objects.all()
    total_price = OrderItem.total_order_price()
    total_quantity = OrderItem.total_quantity()

    return render(request, 'page/buy.html', {"cart": cart, 'total_price': total_price, 'total_quantity':total_quantity})


# def checkout(request):
#     items = []
#     order={'get_cart_total':0, 'get_cart_items':0}
#
#     context = {'items':items,
#                'order':order,
#                }
#     return render(request, 'page/buy.html', context)