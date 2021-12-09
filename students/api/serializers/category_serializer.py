from django.db.models import fields
from rest_framework import serializers

from students.models.category import Category


class Category_Serializer(serializers.ModelSerializer):
    """
        List information of the Student Category:
            id,
            name,

    """
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
        ]
        read_only_field = ['id']
