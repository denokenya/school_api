from django.db.models import fields
from rest_framework import serializers

from student.models.student import Student


class Category_Serializer(serializers.ModelSerializer):
    """
        List information of the Student Category:
            id,
            name,

    """
    class Meta:
        model = Student
        fields = [
            'id',
            'name',
        ]
        read_only_field = ['id']
