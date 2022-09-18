from django.db import models

# Create your models here.

class UserPositions(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    current_position = models.IntegerField()

    @classmethod
    def add_holdings(cls, user_id, event_id, quantity):
        user_position = cls.objects.get_or_create(
            user=user_id,
            event=event_id,
            defaults={'current_position':0}
        )
        user_position.current_holdings += quantity
        if user_position.current_holdings < 0:
            raise Exception("User {} does not have enough holdings to support this trade.".format(user_id))
        user_position.save(update_fields=['current_position'])
