# chat/urls.py
from django.urls import path

from .views import index


urlpatterns = [
    path('live', index, name="index"),
]