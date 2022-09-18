from multiprocessing.sharedctypes import Value
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from orderBook.models import OrderBook
from .models import OrderLinker

@receiver(post_save, sender=OrderBook)
def order_book_post_save(sender, instance, *args, **kwargs):
    """
    Try and match the order placed with existing orders in the book
    """
    # Identify potential matching orders in the order book
    # Repeatedly match as any orders as possible

    if instance.direction == OrderBook.BUY:
        possible_matches = OrderBook.objects.filter(event=instance.event).filter(direction=OrderBook.SELL).filter(price_lte=instance.price).order_by('price', 'submitted')
    else:
        possible_matches = OrderBook.objects.filter(event=instance.event).filter(direction=OrderBook.BUY).filter(price_gte=instance.price).order_by('-price', 'submitted')

    curr_instance = OrderBook.get(pk=instance.id)

    while (curr_instance.quantity > 0) and i < len(possible_matches):
        try:
            OrderLinker.match_orders(curr_instance, possible_matches[i])
        except:
            print("Could not match orders {} and {}".format(curr_instance.order_id, possible_matches[i].order_id))
        finally:
            i += 1
            curr_instance = OrderBook.get(pk=instance.id)
    

