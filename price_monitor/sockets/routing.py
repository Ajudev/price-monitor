from django.urls import re_path

from .consumers import RatesConsumer

websocket_urlpatterns = [
    re_path(r'ws/rates', RatesConsumer.as_asgi()),
]