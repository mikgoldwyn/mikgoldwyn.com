from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.data.get('username').lower()
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is None:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        login(request, user)
        data = serializers.UserSerializer(instance=user).data
        return Response(data)


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        user_serializer = serializers.UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        return Response(serializers.UserSerializer(user).data)


class LogoutView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        logout(request)
        return Response()
