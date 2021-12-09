from django.db.models import fields
from rest_framework import serializers

from students.models.guardian import Guardian


class Guardian_Serializer(serializers.ModelSerializer):
    """
        List information of the Student Guardian


    """

    class Meta:
        model = Guardian
        fields = '__all__'
        read_only_field = ['id']
