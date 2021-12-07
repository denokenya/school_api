from django.db.models import fields
from rest_framework import serializers

from student.models.student import Student


class Student_Serializer(serializers.ModelSerializer):
    """
        List information of the Student :
        admission_no,
        roll_no,
        student_class,
        section,
        first_name,
        last_name,
        gender,
        category,
        religion,
        mobile_number,
        email,
        admission_date,
        blood_group,
        hostel,
        room_number,
        height,
        weight,
        medical_history,
        parent,
        guardian



    """
    class Meta:
        model = Student
        fields = [
            'id',
            'admission_no',
            'roll_no',
            'student_class',
            'section',
            'first_name',
            'last_name',
            'gender',
            'category',
            'religion',
            'mobile_number',
            'email',
            'admission_date',
            'blood_group',
            'hostel',
            'room_number',
            'height',
            'weight',
            'medical_history',
            'parent',
            'guardian',

        ]
        read_only_field = ['id']
