from sqlite3 import IntegrityError
from django.db import models
from django.core import validators
from users.models import CustomUser
from events.models import Event
from django.db import transaction

# Create your models here.

class Order(models.Model):
    OUTCOME_CHOICES = [
        (1, 'Yes'),
        (0, 'No')
    ]
    ORDER_CHOICES = [
        ('M', 'Market'),
        ('P', 'Price')
    ]
    ORDER_DIRECTION = [
        (1, 'Buy'),
        (-1, 'Sell')
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=20, choices=ORDER_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=4, validators=[
                                validators.MaxValueValidator(1, message="Price must be less than $1.00"),
                                validators.MinValueValidator(0, message="Price must be positive")])
    quantity = models.IntegerField(validators=[validators.MinValueValidator(1, message="Must order at least one unit.")])        
    pending_quantity = models.IntegerField(validators=[validators.MinValueValidator(0, message="Order amount cannot be below 0.")])
    filled_quantity = models.IntegerField(default=0)
    outcome = models.CharField(max_length=2, choices=OUTCOME_CHOICES)
    direction = models.CharField(max_length=2, choices=ORDER_DIRECTION)
    time = models.DateTimeField(auto_now=True)
    system_price = models.DecimalField(max_digits=6, decimal_places=4)
    system_direction = models.CharField(max_length=2, choices=ORDER_DIRECTION)
    completed = models.BooleanField(default=False)


    def fill(self, quantity, price):
        """
        Function to fill an order using given price and quantity
        """
        user = self.user
        amount = quantity * price

        # Fill given quantity
        self.pending_quantity -= quantity
        self.filled_quantity += quantity

        if self.pending_quantity == 0:
            self.completed = True

        try:
            with transaction.atomic():
                self.save(update_fields=['pending_quantity', 'filled_quantity', 'completed'])
                user.update_funds(amount)
        except IntegrityError:
            raise ValueError("This order cannot be filled.")
            


