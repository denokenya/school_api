from django.db.models import fields
from rest_framework import serializers

from hostel.models import room_type


class Room_Type_Serializer(serializers.ModelSerializer):
    """
        List information of the Room_Type:
            id,
            name,

    """
    class Meta:
        model = room_type.Room_Type
        fields = [
            'id',
            'name',
        ]
