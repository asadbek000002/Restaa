from django.urls import path
from .views import * 

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('order/', create_order, name='create_order')


]
