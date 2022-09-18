from multiprocessing.sharedctypes import Value
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from orders.models import Order
from django.db import transaction

@receiver(pre_save, sender=Order)
def order_pre_save(sender, instance, *args, **kwargs):
    """
    Confirm that order placed is a valid order.
    """
    return True

    # Check that user has enough funds for a buy order, or enough units for a sell order
    # Deduct the necessary amount of funds and move them to pending funds for the order
    

