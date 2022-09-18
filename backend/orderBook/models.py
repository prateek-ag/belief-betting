from django.core import validators
from django.db import models
from events.models import Event
from django.db import transaction


# Create your models here.

# Model to store the order book

class OrderBook(models.Model):
    MARKET = "M"
    PRICE = "P"
    BUY = "B"
    SELL = "S"

    ORDER_CHOICES = [
        (MARKET, 'Market'),
        (PRICE, 'Price')
    ]
    ORDER_DIRECTION = [
        (BUY, 'Buy'),
        (SELL, 'Sell')
    ]


    order = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    submitted = models.DateTimeField(auto_now=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    fill_type = models.CharField(max_length=20, choices=ORDER_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=4)
    direction = models.CharField(max_length=2, choices=ORDER_DIRECTION)                      
    quantity = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['order_id'], name='unique order_id')
        ]

    def fill_order(self, quantity, price):
        self.quantity -= quantity
        with transaction.atomic():
            self.order.fill(quantity, price)
            self.save(update_fields=['quantity'])
            if self.quantity == 0:
                self.delete()


