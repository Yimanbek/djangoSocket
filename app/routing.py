from django.urls import re_path
from .consumers import NotifyConsumer

websocket_urlpatterns = [
    re_path(r"^ws/notify/$", NotifyConsumer.as_asgi()),
]
