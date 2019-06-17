from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Attendance(models.Model):
    date = models.DateField(auto_now_add=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='attendances')

    class Meta:
        unique_together = [['date', 'student']]
