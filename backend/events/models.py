from django.db import models

# Model for a single betting event

CAT_CHOICES = ['Crypto', 'Sports', 'Business', 'Economics', 'Other']


class Event(models.Model):
    
    name = models.CharField(max_length=120)
    description = models.TextField(default="")
    resolution = models.TextField(default="")
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()
    updated_on = models.DateField(auto_now=True)
    created_on = models.DateField()
    category = models.CharField(max_length=30)
    true_label = models.CharField(max_length=30)
    false_label = models.CharField(max_length=30)
    true_price = models.DecimalField(max_digits=4, decimal_places=2, default=0.5)
    false_price = models.DecimalField(max_digits=4, decimal_places=2, default=0.5)
    volume = models.IntegerField(default=0)
