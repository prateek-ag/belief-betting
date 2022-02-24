from multiprocessing.sharedctypes import Value
from django.dispatch import receiver
from django.db.models.signals import pre_save
from orders.models import Order
from django.db.models import Sum

@receiver(pre_save, sender=Order)
def order_pre_save(sender, instance, *args, **kwargs):
    """
    Check if the user can support the order that was placed
    """
    user = instance.user
    if instance.direction == 1:
        price = instance.price * instance.quantity
        if price > user.funds:
            raise ValueError("Not enough funds")
    
    elif instance.direction == 0:
        return
        event = instance.event
        user_units = user.bet_set.filter(event=event).aggregate(Sum('quantity'))['quantity__sum']
        if instance.quantity > user_units:
            raise ValueError("Not enough units")