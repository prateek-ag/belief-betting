from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import OrderSerializer
from .models import Event
from rest_framework.permissions import AllowAny, IsAuthenticated

class PlaceOrder(APIView):
    """
    Place an order for a bet
    """
    permission_classes = [IsAuthenticated,]
    serializer = None

    def post(self, request):
        serializer = OrderSerializer(data=request.data, user=request.user)
        if serializer.is_valid():
            order = serializer.save()
            if order:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)