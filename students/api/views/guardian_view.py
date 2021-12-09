from rest_framework import authentication, permissions, filters
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from students.api.serializers.guardian_serializer import Guardian_Serializer


from students.models.guardian import Guardian

from mixins .apimixin import DefaultMixin


class Guardian_ViewSet(DefaultMixin, ModelViewSet):

    """Guardian API End points."""

    queryset = Guardian.objects.all()
    serializer_class = Guardian_Serializer
