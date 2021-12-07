from django.db.models import fields
from rest_framework import serializers

from hostel.models.hostel import Hostel


class Hostel_Serializer(serializers.ModelSerializer):
    """
        List information of the hostel:
            id,
            name,
            room_type,

    """
    class Meta:
        model = Hostel
        fields = [
            'id',
            'name',
            'room_type',

        ]
        read_only_field = ['id']
