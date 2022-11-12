from rest_framework import routers
from django.urls import path, include
from .views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'quotes', PriceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]