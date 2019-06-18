from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.last_name.title()}, {self.user.first_name.title()}'


class Attendance(models.Model):
    date = models.DateField(auto_now_add=True)
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='attendances')

    class Meta:
        unique_together = [['date', 'student']]

    def __str__(self):
        return f'{self.student} ({self.date.strftime("%A, %d %B %Y")})'
