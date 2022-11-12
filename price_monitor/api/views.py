from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from utils.mixins import ExceptionMixin
from .serializers import PriceSerializer
from .models import Price
from .helpers import fetch_rates


class PriceViewSet(ExceptionMixin, ModelViewSet):
    """
    Viewset which will handle fetching and displaying of price rates
    """
    serializer_class = PriceSerializer
    queryset = Price.objects.all()
    http_method_names = ['get', 'post']
    permission_classes = [permissions.IsAuthenticated, ]

    def create(self, request, *args, **kwargs):
        rates_data = fetch_rates()
        serializer = self.get_serializer(data=rates_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(rates_data, status=status.HTTP_201_CREATED)
