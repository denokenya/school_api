from django.db.models import fields
from rest_framework import serializers

from student.models.guardian import Guardian


class Guardian_Serializer(serializers.ModelSerializer):
    """
        List information of the Student Guardian:
            id,
            name,
            mobile_phone,
            occupation,
            relation,
            email,
            current_address,
            parmanent_address,


    """
    class Meta:
        model = Guardian
        fields = [
            'id',
            'name',
            'mobile_phone',
            'occupation',
            'relation',
            'email',
            'current_address',
            'parmanent_address',
        ]
        read_only_field = ['id']
