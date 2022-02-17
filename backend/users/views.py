from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated

# Create your views here.

class CustomUserRegister(APIView):
    """
    Register a new user
    """
    permission_classes = [AllowAny,]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomUserDashboard(APIView):
    """
    Get user info
    """
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        return Response(data={"first_name": request.user.first_name, "last_name": request.user.last_name}, status=status.HTTP_200_OK)