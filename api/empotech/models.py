from django.contrib.auth.models import User
from django.db import models
from model_utils import Choices


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.last_name.title()}, {self.user.first_name.title()}'


class Attendance(models.Model):
    date = models.DateField(auto_now_add=True)

    # Related fields
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='attendances')

    class Meta:
        unique_together = [['date', 'student']]

    def __str__(self):
        return f'{self.student} ({self.date.strftime("%A, %d %B %Y")})'

    def date_display(self):
        return f'{self.date.strftime("%A, %d %B %Y")}'


class Grade(models.Model):
    TYPES = Choices(
        ('activity', 'Activity'),
    )

    score = models.PositiveSmallIntegerField()
    total = models.PositiveSmallIntegerField()
    type = models.CharField(choices=TYPES, max_length=25)

    # Related fields
    student = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='grades')

    def __str__(self):
        return f'{self.student.user.get_full_name().title()} -- {self.get_type_display()} ({self.score}/{self.total})'
