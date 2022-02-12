from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import CustomUserRegister

urlpatterns = [
    path('token/get/', jwt_views.TokenObtainPairView.as_view(), name='token_create'), 
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/register/', CustomUserRegister.as_view(), name="register_user")
]