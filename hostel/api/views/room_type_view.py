from rest_framework import authentication, permissions, filters
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from hostel.api.serializers.room_type_serializer import Room_Type_Serializer


from hostel.models import room_type

from mixins .apimixin import DefaultMixin


class Room_Type_ViewSet(DefaultMixin, ModelViewSet):

    """Room Type API End points."""
    queryset = room_type.Room_Type.objects.all()
    serializer_class = Room_Type_Serializer
    search_fields = ('name',)
    ordering = ('name',)
