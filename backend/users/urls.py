from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import CustomUserRegister, CustomUserDashboard

urlpatterns = [
    path('token/get/', jwt_views.TokenObtainPairView.as_view(), name='token_create'), 
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', CustomUserRegister.as_view(), name="register_user"),
    path('dashboard/', CustomUserDashboard.as_view(), name="dasboard_user"),
]