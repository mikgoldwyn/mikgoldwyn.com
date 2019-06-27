from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from . import models
from . import related_serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    student = related_serializers.RelatedStudentSerializer(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'student', 'is_superuser', 'token')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.pop('username'),
            email=self.initial_data.get('email', None),
            password=validated_data.pop('password'),
            **validated_data,
        )
        models.Student.objects.create(user=user)
        return user

    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key


class StudentSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)

    class Meta:
        model = models.Student
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    student_display = serializers.CharField(source='student.__str__', read_only=True)

    class Meta:
        model = models.Grade
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    student_display = serializers.CharField(source='student.__str__', read_only=True)
    date_display = serializers.CharField(read_only=True)

    class Meta:
        model = models.Attendance
        fields = '__all__'
