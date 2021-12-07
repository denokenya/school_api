from rest_framework import authentication, permissions, filters
import django_filters.rest_framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from student.api.serializers.student_serializer import Student_Serializer


from student.models.student import Student

from mixins .apimixin import DefaultMixin


class Student_ViewSet(DefaultMixin, ModelViewSet):

    """Student Type API End points."""
    queryset = Student.objects.all()
    serializer_class = Student_Serializer
    search_fields = ('admission_no',)
    ordering = ('admission_no',)
