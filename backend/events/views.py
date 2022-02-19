from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EventSummarySerializer, EventDetailSerializer
from .models import Event
from rest_framework.permissions import AllowAny, IsAuthenticated

class EventList(APIView):
    """
    List all the events, or create a new event
    """
    permission_classes = [AllowAny,]
    serializer = None

    def get(self, request):
        try:
            events = Event.objects.all().order_by('end_date')
            serializer = EventSummarySerializer(events, many=True, context={'request': request})
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data)

class DetailedEvent(APIView):
    """
    Get the details of a single event
    """
    permission_classes = [AllowAny,]

    def get(self, request, pk):
        try:
            event = Event.objects.get(id=pk)
            serializer = EventDetailSerializer(event, context={'request': request})
        except:
            return Response("Event with ID " + str(pk) + " does not exist.", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data)