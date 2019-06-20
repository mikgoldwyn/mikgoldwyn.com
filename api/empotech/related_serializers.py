from rest_framework import serializers

from . import models


class RelatedStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        exclude = ('user', )
