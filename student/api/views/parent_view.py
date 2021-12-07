from rest_framework import authentication, permissions, filters
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from student.api.serializers.parent_serializer import Parent_Serializer


from student.models.parent import Parent

from mixins .apimixin import DefaultMixin


class Parent_ViewSet(DefaultMixin, ModelViewSet):

    """Room Type API End points."""
    queryset = Parent.objects.all()
    serializer_class = Parent_Serializer
    search_fields = ('father_name',)
    ordering = ('father_name',)
