from django.shortcuts import render, redirect, get_object_or_404
from .models import *

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'page/index.html')


def category_list(request):
    menu = Menu.objects.all()
    return render(request, 'page/menu_list.html', {'menu': menu})




def meal_detail(request, ):
    meal = Meal.objects.all()
    context = {
        'meal': meal,
    }
    return render(request, 'page/meal_detail.html', context)

def product_list(request, category_slug):
    menu = Menu.objects.get(slug=category_slug)
    meal = Meal.objects.filter(menu=menu)
    return render(request, 'page/product_lis.html', {'menu': menu, 'meal': meal})



def add_to_cart(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, meal=meal)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def cart(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'cart.html', {'cart_items': cart_items, 'cart': cart})

def remove_from_cart(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.get(cart=cart, meal=meal)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')