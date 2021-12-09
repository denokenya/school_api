from django.db.models import fields
from rest_framework import serializers

from students.models.student import Student


class Student_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
        read_only_field = ['id']
