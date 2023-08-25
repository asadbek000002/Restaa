from django.shortcuts import render, HttpResponse
from purchase.models import OrderItem
# Create your views here.
def index(request):
    return HttpResponse("Salom")

def total(request):
    total_price = OrderItem.total_order_price()
    total_quantity = OrderItem.total_quantity()

    return render(request, 'page/buy.html', { 'total_price': total_price, 'total_quantity':total_quantity})