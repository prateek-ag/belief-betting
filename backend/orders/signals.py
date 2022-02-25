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

    param_dict = {
        'm_sd': instance.system_direction * -1,
        'sp': instance.system_price,
        'e': instance.event,
    }

    matching_query = """SELECT * FROM orders_order WHERE
                            completed = false AND event = %(e)s 
                            AND system_direction = %(m_sd)s AND system_price <= %(sp)s
                        ORDER BY 
                            system_price, time"""
    
    while True:
        try:
            with transaction.atomic():
                # Exit if order is completely filled
                order = Order.objects.select_related().select_for_update().get(id=instance.id)
                if order.completed: break

                # Exit if no more orders is no longer fillable
                matching_orders = Order.objects.select_for_update().select_related().raw(matching_query, params=param_dict)
                if len(matching_orders) == 0: break

                matching_order = matching_orders[0]
                matching_quantity = min(instance.pending_quantity, matching_order.pending_quantity)
                matching_price = matching_order.price
                matching_order.fill(matching_quantity, matching_price)
                order.fill(matching_quantity, matching_price)
        except:
            print("Order could not be filled")