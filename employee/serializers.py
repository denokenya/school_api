from rest_framework import serializers
from .models import Designation, Department, Role, Employee


class DesignationSerializer(serializers.ModelSerializer):
    """Designation serializer which serializes all the fields of the designation model """

    class Meta:
        model = Designation
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    """Department  serializer which serializes all the fields of the department model """

    class Meta:
        model = Department
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    """Role serializer  which serializes all the fields of the role model"""

    class Meta:
        model = Role
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    """Employee serializer which serializes all the fields of the employee model"""

    class Meta:
        model = Employee
        fields = '__all__'
