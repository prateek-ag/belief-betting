from rest_framework import serializers
from events.models import Event
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse



class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ('id', 'name', 'description', 'start_date', 'end_date', 'updated_on', 'created_on', 'category', 'true_label', 'false_label')