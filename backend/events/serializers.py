from rest_framework import serializers
from events.models import Event


class EventSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'start_date', 'end_date', 'category', 'true_price', 'false_price', 'volume')

class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'