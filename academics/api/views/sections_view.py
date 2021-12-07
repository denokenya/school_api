from rest_framework import authentication, permissions, filters
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from academics.api.serializers.sections_serializer import Section_Serializer


from academics.models.sections import Section

from mixins .apimixin import DefaultMixin


class Section_ViewSet(DefaultMixin, ModelViewSet):

    """Hostel Rooms API End points."""
    queryset = Section.objects.all()
    serializer_class = Section_Serializer
    search_fields = ('name',)
    ordering = ('name',)
