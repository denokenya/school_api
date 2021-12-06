from rest_framework import authentication, permissions, filters
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Employee, Designation, Department, Role
from .serializers import EmployeeSerializer, DepartmentSerializer, DesignationSerializer, RoleSerializer


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


class DesignationViewSet(DefaultMixin, ModelViewSet):
    """Designation ViewSet that provides default create(), retrieve(), update(), partial_update(), destroy() 
    and list() actions"""
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)


class DepartmentViewSet(DefaultMixin, ModelViewSet):
    """Department ViewSet that provides default create(), retrieve(), update(), partial_update(), destroy() 
    and list() actions"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)


class RoleViewSet(DefaultMixin, ModelViewSet):
    """Role ViewSet that provides default create(), retrieve(), update(), partial_update(), destroy() 
    and list() actions."""
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)


class EmployeeViewSet(DefaultMixin, ModelViewSet):
    """Employee ViewSet that provides default create(), retrieve(), update(), partial_update(), destroy()
     and list() actions."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    search_fields = ('employeeID',)
    ordering_fields = ('employeeID',)
