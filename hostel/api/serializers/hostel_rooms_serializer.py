from django.db.models import fields
from rest_framework import serializers

from hostel.models.hostel_rooms import Rooms

from .hostel_serializer import Hostel_Serializer


class Hostel_Room_Serializer(serializers.ModelSerializer):
    """
        List information of the Hostel Rooms Number:
            id,
            name,
            room_number,


    """
    hostels = Hostel_Serializer(many=True, read_only=True, required=False)

    class Meta:

        model = Rooms
        fields = [
            'id',
            'name',
            'hostels',
        ]
        read_only_field = ['id']
