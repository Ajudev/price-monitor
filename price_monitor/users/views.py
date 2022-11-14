from rest_framework.viewsets import GenericViewSet
from .serializers import UserSerializer

from utils.mixins import ExceptionMixin
from rest_framework.mixins import CreateModelMixin
# from rest_framework.response import Response
# from rest_framework import permissions, status
from rest_framework.decorators import action
# from django.contrib.auth import logout
from rest_framework_simplejwt import views as jwt_views


class AuthViewSet(ExceptionMixin, CreateModelMixin, GenericViewSet):
    """
    Viewset for authentication of users which includes registration/create JWT token/refresh JWT token
    """
    serializer_class = UserSerializer

    @action(methods=['POST', ], detail=False)
    def register(self, request):
        data = {
            "message": "User has been created successfully"
        }
        response = self.create(request)
        response.data = data
        return response

    @action(methods=['POST', ], detail=False)
    def token(self, request):
        return jwt_views.TokenObtainPairView.as_view()(request=request._request)

    @action(methods=['POST', ], detail=False)
    def refresh(self, request):
        return jwt_views.TokenRefreshView.as_view()(request=request._request)
