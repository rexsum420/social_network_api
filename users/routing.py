from django.urls import path
from .consumers import UserActivityConsumer

websocket_urlpatterns = [
    path('ws/activity/', UserActivityConsumer.as_asgi()),
]