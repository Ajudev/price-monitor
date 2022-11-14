from django.core.paginator import Paginator
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
        """
        Method which will be invoked when post method gets called
        """
        
        rates_data = fetch_rates()
        serializer = self.get_serializer(data=rates_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(rates_data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        """
        Method which will be invoked when get method gets called
        """
        content_per_page = request.GET.get('per_page', None)
        queryset = self.filter_queryset(self.get_queryset())
        if content_per_page:
            page_number = request.GET.get('page', 1)
            paginate = Paginator(queryset, per_page=int(content_per_page))
            paginate_data = paginate.get_page(page_number)
            return Response({"total_pages": paginate.num_pages, "data":paginate_data.object_list.values()}, status=status.HTTP_200_OK)

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
