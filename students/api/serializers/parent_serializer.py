from django.db.models import fields
from rest_framework import serializers

from students.models.parent import Parent


class Parent_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Parent
        fields = '__all__'
        read_only_field = ['id']
