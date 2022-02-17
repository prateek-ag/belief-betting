from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EventSerializer
from .models import Event
from rest_framework.permissions import AllowAny, IsAuthenticated

class EventList(APIView):
    """
    List all the events, or create a new event
    """
    permission_classes = [AllowAny,]

    def get(self, request):
        events = Event.objects.all().order_by('end_date')
        serializer = EventSerializer(events, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)