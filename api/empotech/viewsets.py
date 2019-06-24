from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers
from . import models


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

    @action(detail=True, methods=['post'], url_path='add-attendance', permission_classes=[permissions.AllowAny])
    def add_attendance(self, request, pk):
        user = self.get_object()
        try:
            models.Attendance.objects.create(student=user.student)
            created = True
        except IntegrityError:
            created = False

        return Response({
            'user_full_name': f'{user.get_full_name().title()}',
            'created': created,
        })


class GradeViewset(viewsets.ModelViewSet):
    queryset = models.Grade.objects.all()
    serializer_class = serializers.GradeSerializer

    def get_queryset(self):
        queryset = self.queryset
        if not self.request.user.is_superuser and hasattr(self.request.user, 'student'):
            queryset.filter(student=self.request.user.student)
        return queryset
