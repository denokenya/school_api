from rest_framework import authentication, permissions, filters
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from hostel.api.serializers.hostel_rooms_serializer import Hostel_Room_Serializer


from hostel.models.hostel_rooms import Rooms

from mixins .apimixin import DefaultMixin


class Hostel_Room_ViewSet(DefaultMixin, ModelViewSet):

    """Hostel Rooms API End points."""
    queryset = Rooms.objects.all()
    serializer_class = Hostel_Room_Serializer
    search_fields = ('name',)
    ordering = ('name',)
