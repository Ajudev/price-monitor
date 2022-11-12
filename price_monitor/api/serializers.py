from rest_framework.serializers import ModelSerializer
from .models import Price


class PriceSerializer(ModelSerializer): 
    """
    Serializer for Price Model
    """


    class Meta:
        """
        Meta data class
        """
        model = Price
        fields = '__all__'