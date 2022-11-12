from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    """
    Model Serializer to validate all input data before storing it to the DB
    """

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        """
        Meta data class
        """
        model = User
        fields = ('id', 'username', 'email', 'password')