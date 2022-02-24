from multiprocessing.sharedctypes import Value
from django.dispatch import receiver
from django.db.models.signals import pre_save
from orders.models import Order
from datetime import datetime

@receiver(pre_save, sender=Order)
def order_pre_save(sender, instance, *args, **kwargs):
    """
    Check that the event being bet on has not expired
    """
    if datetime.now() > instance.event.end_date:
        raise ValueError("The event has expired")

    if datetime.now() < instance.event.start_date:
        raise ValueError("The event has not yet started")