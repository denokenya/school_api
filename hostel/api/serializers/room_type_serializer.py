from django.db.models import fields
from rest_framework import serializers

from hostel.models.room_type import Room_Type


class Room_Type_Serializer(serializers.ModelSerializer):
    """
        List information of the Room_Type:
            id,
            name,

    """
    class Meta:
        model = Room_Type
        fields = [
            'id',
            'name',
        ]
        read_only_field = ['id']
