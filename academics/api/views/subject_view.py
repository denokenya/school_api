from rest_framework import authentication, permissions, filters
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from academics.api.serializers.subject_serializer import Subject_Serializer


from academics.models.subjects import Subject

from mixins .apimixin import DefaultMixin


class Subject_ViewSet(DefaultMixin, ModelViewSet):

    """Hostel Rooms API End points."""
    queryset = Subject.objects.all()
    serializer_class = Subject_Serializer
    search_fields = ('name',)
    ordering = ('name',)
