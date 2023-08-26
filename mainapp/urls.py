from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('categories/', category_list, name='category_list'),
    path('categories/<slug:category_slug>/', product_list, name='product_list'),
    path('meal/', meal_detail, name='meal_detail'),
    path('add_to_cart/<int:meal_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart, name='cart'),
    path('remove_from_cart/<int:meal_id>/', remove_from_cart, name='remove_from_cart'),
]