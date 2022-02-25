from tkinter import Place
from django.urls import path
from .views import PlaceOrder, TestView

urlpatterns = [
    path('place/', PlaceOrder.as_view(), name='place_order'), 
    path('test/', TestView.as_view(), name='test_view'), 
]