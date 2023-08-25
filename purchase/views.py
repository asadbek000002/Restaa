from django.shortcuts import render, redirect

from .forms import *
# Create your views here.


def checkout(request):
    cart = OrderItem.objects.all()
    total_price = OrderItem.total_order_price()
    total_quantity = OrderItem.total_quantity()

    return render(request, 'page/buy.html', {"cart": cart, 'total_price': total_price, 'total_quantity':total_quantity})


def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("checkout")
    else:
        form = OrderForm()
    return render(request, 'page/catr_order.html', {'form': form})