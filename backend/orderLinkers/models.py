from django.db import models
from orders.models import Order
from django.core import validators
from django.db import transaction


# Create your models here.
# Table to represent orders that have been matched up and executed

class OrderLinker(models.Model):
    order_1 = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='linker_order_1')
    order_2 = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='linker_order_2')
    fill_quantity = models.IntegerField([validators.MinValueValidator(1, message="Must fill at least one unit!")]) 
    fill_price = models.DecimalField(decimal_places=4, max_digits=10)
    datetime_filled = models.DateTimeField(auto_now=True)
    comission_order_1 = models.DecimalField(decimal_places=2, max_digits=6)
    comission_order_2 = models.DecimalField(decimal_places=2, max_digits=6)

    @classmethod
    def match_orders(cls, order_1_book, order_2_book):
        if cls.check_orders_can_be_linked(order_1_book, order_2_book):
            price = None
            quantity = min(order_1_book.quantity, order_2_book.quantity)
            with transaction.atomic():
                order_1_book.fill_order(quantity, price)
                order_2_book.fill_order(quantity, price)
                cls.create(order_1_id=order_1_book.order_id, order_2_id=order_2_book.order_id, fill_quantity=quantity, fill_price=price)
        else:
            raise Exception("Orders cannot be linked.")

    @classmethod
    def check_orders_can_be_linked(cls, order_1_book, order_2_book):
        if order_1_book.event != order_2_book.event: return False
        if order_1_book.direction * order_2_book.direction != -1: return False

        if order_1_book.fill_type == Order.MARKET or order_2_book.fill_type == Order.MARKET: return True

        # If order_1 is a buy order, but the bid price is less than the ask price of order_2, the orders cannot be matched
        if order_1_book.direction == Order.BUY:
            if order_1_book.price < order_2_book.price: return False

        # If order_2 is a sell order, but the ask price is greater than the bid price of order_2, the orders cannot be matched
        if order_1_book.direction == Order.SELL:
            if order_1_book.price > order_2_book.price: return False

        return True


