from rest_framework import serializers
from events.models import Event
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse



class EventSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'start_date', 'end_date', 'category', 'true_price', 'false_price', 'volume')

class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'