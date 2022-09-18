from django.db import models
from django.core import validators
from users.models import CustomUser
from events.models import Event
from orderBook.models import OrderBook
from django.db import transaction
from django.apps import apps
from userPositions.models import UserPositions

# Create your models here.

class Order(models.Model):
    YES = "Y"
    NO = "N"
    MARKET = "M"
    PRICE = "P"
    BUY = "B"
    SELL = "S"
    COMPLETED = "COMPLETED"
    OPEN = "OPEN"
    CANCELLED = "CACNCELLED"

    OUTCOME_CHOICES = [
        (YES, 'Yes'),
        (NO, 'No')
    ]
    ORDER_CHOICES = [
        (MARKET, 'Market'),
        (PRICE, 'Price')
    ]
    ORDER_DIRECTION = [
        (BUY, 'Buy'),
        (SELL, 'Sell')
    ]

    STATUS_CHOICES = [
        (COMPLETED, "Completed"),
        (OPEN, "Open"),
        (CANCELLED, "Cancelled")
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=20, choices=ORDER_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=4, validators=[
                                validators.MaxValueValidator(1, message="Price must be less than $1.00"),
                                validators.MinValueValidator(0, message="Price must be positive")])
    quantity = models.IntegerField(validators=[validators.MinValueValidator(1, message="Must order at least one unit.")])        
    pending_quantity = models.IntegerField(validators=[validators.MinValueValidator(0, message="Order amount cannot be below 0.")])
    filled_quantity = models.IntegerField(default=0)
    pending_funds = models.DecimalField(max_digits=100, decimal_places=2)
    outcome = models.CharField(max_length=10, choices=OUTCOME_CHOICES)
    direction = models.CharField(max_length=10, choices=ORDER_DIRECTION)
    time = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, default=OPEN, choices=STATUS_CHOICES)


    def fill(self, quantity, price):
        """
        Fill an order using given price and quantity
        """
        if self.pending_quantity < quantity:
            raise Exception("Cannot fill given quantity.")
        if self.status == self.CANCELLED:
            raise Exception("Order has already been cancelled.")

        amount = quantity * price

        # Fill given quantity
        self.pending_quantity -= quantity
        self.filled_quantity += quantity
        self.pending_funds -= amount

        with transaction.atomic():
            if self.pending_quantity == 0:
                self.complete_order()
            self.user.update_position(self.event, quantity, amount)
            self.save(update_fields=['pending_quantity', 'filled_quantity', 'status', 'pending_funds'])
        

    def complete(self):
        if self.status == self.CANCELLED:
            raise Exception("Order has already been cancelled.")
        if self.status == self.COMPLETED:
            raise Exception("Order has already been completed.")

        self.status = self.COMPLETED
        remaining_pending_funds = self.pending_funds
        self.pending_funds = 0
        with transaction.atomic():
            self.user.add_funds(remaining_pending_funds)
            self.save(update_fields=['pending_funds'])

    def cancel(self):
        if self.status == self.COMPLETED:
            raise Exception("Order has already been completed.")
        if self.status == self.CANCELLED:
            raise Exception("Order has already been cancelled.")

        self.status = self.CANCELLED
        remaining_pending_funds = self.pending_funds
        self.pending_funds = 0

        with transaction.atomic():
            OrderBook.objects.filter(order_id=self.id).delete()
            self.user.add_funds(remaining_pending_funds)
            self.save(update_fields=['pending_funds'])




