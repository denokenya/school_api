from rest_framework import authentication, permissions, filters
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from students.api.serializers.category_serializer import Category_Serializer


from students.models.category import Category

from mixins .apimixin import DefaultMixin


class Category_ViewSet(DefaultMixin, ModelViewSet):

    """Room Type API End points."""
    queryset = Category.objects.all()
    serializer_class = Category_Serializer
    search_fields = ('name',)
    ordering = ('name',)
