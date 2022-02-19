from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import EventList, DetailedEvent

urlpatterns = [
    path('', EventList.as_view(), name='event-list'), 
    path('<int:pk>', DetailedEvent.as_view(), name='detailed-event'),
]