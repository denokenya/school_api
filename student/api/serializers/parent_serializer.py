from django.db.models import fields
from rest_framework import serializers

from student.models.parent import Parent


class Parent_Serializer(serializers.ModelSerializer):
    """
        List information of the Student Parents:
            id,
            father_name,
            father_phone,
            father_occupation,
            mother_name,
            mother_phone,
            mother_occupation,


    """
    class Meta:
        model = Parent
        fields = [
            'father_name',
            'father_phone',
            'father_occupation',
            'mother_name',
            'mother_phone',
            'mother_occupation',

        ]
        read_only_field = ['id']
