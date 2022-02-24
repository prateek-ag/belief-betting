from tkinter import Place
from django.urls import path
from .views import PlaceOrder

urlpatterns = [
    path('place/', PlaceOrder.as_view(), name='place_order'), 
]