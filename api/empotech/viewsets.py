from django.contrib.auth.models import User
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        queryset = self.queryset
        if not self.request.user.is_superuser:
            queryset.filter(id=self.request.user.id)
        return queryset

    @action(detail=False)
    def me(self, request):
        return Response(self.get_serializer(request.user).data)

    @action(detail=False, methods=['post'], url_path='add-attendance', permission_classes=[permissions.AllowAny])
    def add_attendance(self, request):
        if request.data['secret_key'] != 'a_very_secret_key':
            return Response(status=status.HTTP_401_UNAUTHORIZED, data='Invalid secret key')
        user = User.objects.get(id=request.data['user_id'])
        user.student.attendance.create()
        return Response()
