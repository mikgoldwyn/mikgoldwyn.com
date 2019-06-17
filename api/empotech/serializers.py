from django.contrib.auth.models import User
from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data.pop('username'),
            email=self.initial_data.get('email', None),
            password=validated_data.pop('password'),
            **validated_data,
        )
        models.Student.objects.create(user=user)
        return user


class StudentSerializer(serializers.ModelSerializer):
    user_data = UserSerializer(source='user', read_only=True)

    class Meta:
        model = models.Student
        fields = '__all__'
