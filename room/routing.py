from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/<int:id>/', consumers.ChatComsumer.as_asgi()),
]
