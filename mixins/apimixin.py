from rest_framework import authentication, permissions, filters
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class DefaultMixin(object):
    """Default settings for view authentication,permissions,filtering and pagination.
    DefaultMixin will be one of the base classes for the API view classes to define these options"""

    authentication_classes = (
        # authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = [filters.SearchFilter]