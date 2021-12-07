from rest_framework import serializers
from academics.models.subject_group import Subject_Group


class Subject_Group_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Subject_Group
        fields = '__all__'
        read_only_field = ['id']
