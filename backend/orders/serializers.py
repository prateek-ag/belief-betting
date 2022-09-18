from re import L
from rest_framework import serializers
from django.db import transaction
from orders.models import Order

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('__all__')

    # Custom initializer to define system calculated values for the order
    def __init__(self, *args, user, data, **kwargs):
        data['user'] = user
        data['pending_quantity'] = data['quantity']
        data['system_price'] = self.get_system_price(data)
        data["system_direction"] = self.get_system_direction(data)
        super(OrderSerializer, self).__init__(data=data, *args, **kwargs)

    # For order matching purposes, all orders are converted into "YES" outcome orders.
    # Buying "NO" at price x == Selling "YES" at price (1-x)
    # Selling "NO" at price x == Buying "YES" at price (1-x)

    def get_system_price(self, data):
        if data["outcome"] == 0:
            return (1 - data["price"])
        return data["price"]

    def get_system_direction(self, data):
        if data["outcome"] == 0:
            if data["direction"] == 0:
                return 1
            return 0
        return data["direction"]




