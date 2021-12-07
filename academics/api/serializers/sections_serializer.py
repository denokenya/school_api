from rest_framework import serializers
from academics.models.sections import Section


class Section_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Section
        fields = '__all__'
        read_only_field = ['id']
