from rest_framework import authentication, permissions, filters
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from academics.api.serializers.subject_group_serializer import Subject_Group_Serializer


from academics.models.subject_group import Subject_Group

from mixins .apimixin import DefaultMixin


class Subject_Group_ViewSet(DefaultMixin, ModelViewSet):

    queryset = Subject_Group.objects.all()
    serializer_class = Subject_Group_Serializer
    search_fields = ('name',)
    ordering = ('name',)
