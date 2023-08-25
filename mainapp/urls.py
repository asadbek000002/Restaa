from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('categories/', category_list, name='category_list'),
    path('categories/<slug:category_slug>/', product_list, name='product_list'),
    path('meal/<int:pk>/', meal_detail, name='meal_detail'),
]