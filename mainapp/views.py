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

def product_list(request, category_slug):
    menu = Menu.objects.get(slug=category_slug)
    meal = Meal.objects.filter(menu=menu)
    return render(request, 'page/product_lis.html', {'menu': menu, 'meal': meal})



def meal_detail(request, pk=None):
    meal = Meal.objects.filter(pk=pk)
    context = {
        'meal': meal,
    }
    return render(request, 'page/meal_detail.html', context)


