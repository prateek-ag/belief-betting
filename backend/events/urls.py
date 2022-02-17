from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import EventList

urlpatterns = [
    path('', EventList.as_view(), name='event-list'), 

]