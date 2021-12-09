from rest_framework import authentication, permissions, filters
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from students.api.serializers.parent_serializer import Parent_Serializer


from students.models.parent import Parent

from mixins .apimixin import DefaultMixin


class Parent_ViewSet(DefaultMixin, ModelViewSet):

    """Parent API End points."""

    queryset = Parent.objects.all()
    serializer_class = Parent_Serializer
