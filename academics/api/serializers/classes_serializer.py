from django.db.models import fields
from rest_framework import serializers

from academics.models.classes import Classes


class Classes_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Classes
        fields = '__all__'
        read_only_field = ['id']
