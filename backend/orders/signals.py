from multiprocessing.sharedctypes import Value
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from orders.models import Order
from django.db import transaction

@receiver(post_save, sender=Order)
def order_post_save(sender, instance, *args, **kwargs):
    """
    Order matching and filling once the order has been posted
    """

    matching_order = None
    matching_quantity = min(instance.pending_quantity, matching_order.pending_quantity)

    if instance.direction == 1:
        matching_price = min(instance.price, matching_order.price)
    else:
        matching_price = max(instance.price, matching_order.price)
        
    try:
        with transaction.atomic():
            matching_order.fill(matching_quantity, matching_price)
            instance.fill(matching_quantity, matching_price)
    except:
        print("Order could not be filled")