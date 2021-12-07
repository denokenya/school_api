from rest_framework import authentication, permissions, filters
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from academics.api.serializers.classes_serializer import Classes_Serializer


from academics.models.classes import Classes

from mixins .apimixin import DefaultMixin


class Classes_ViewSet(DefaultMixin, ModelViewSet):

    queryset = Classes.objects.all()
    serializer_class = Classes_Serializer
    search_fields = ('name',)
    ordering = ('name',)
