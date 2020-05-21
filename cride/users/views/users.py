"""Users Views."""

# Django REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializer
from cride.users.serializers import (
    UserLoginSerializer,
    UserModelSerializer,
    UserSignUpSerializer,
)


class UserLoginAPIView(APIView):
    """User login View."""

    def post(self, request, *args, **kwargs):
        """Handle HTTP request."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'status': '200',
            'token': token,
        }
        return Response(data, status=status.HTTP_201_CREATED)


class UserSignUpAPIView(APIView):
    """User Sign Up View."""

    def post(self, request, *args, **kwargs):
        """Handle HTTP request."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'status': '200',
        }
        return Response(data, status=status.HTTP_201_CREATED)
