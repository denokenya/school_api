from rest_framework import serializers
from academics.models.subjects import Subject


class Subject_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Subject
        fields = '__all__'
        read_only_field = ['id']
