from django.contrib import admin
from .models import Event
# Register your models here.

class EventAdmin(admin.ModelAdmin):
    model = Event

admin.site.register(Event, EventAdmin)