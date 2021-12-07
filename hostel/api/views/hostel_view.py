from rest_framework import authentication, permissions, filters
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from hostel.api.serializers.hostel_serializer import Hostel_Serializer


from hostel.models.hostel import Hostel

from mixins .apimixin import DefaultMixin


class Hostel_ViewSet(DefaultMixin, ModelViewSet):

    """Hostel API End points."""
    queryset = Hostel.objects.all()
    serializer_class = Hostel_Serializer
    search_fields = ('name',)
    ordering = ('name',)
