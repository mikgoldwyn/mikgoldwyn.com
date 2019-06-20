from django.contrib.auth.models import User
from rest_framework import viewsets
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

    @action(detail=True, methods=['post'], url_path='add-attendance')
    def add_attendance(self, request, id):
        user = self.get_object()
        user.student.attendance.create()
        return Response()
