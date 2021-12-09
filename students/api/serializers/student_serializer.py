from django.db.models import fields
from rest_framework import serializers
from students.models.category import Category

from students.models.student import Student
from hostel.models.hostel import Hostel
from hostel.models.hostel_rooms import Rooms
from students.models.guardian import Guardian
from students.models.parent import Parent


class Student_Serializer(serializers.ModelSerializer):
    """
        List information of the Student :


    """
    # We want to display the student category's name instead of the id.
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='name')

    # We want to display the hostel's name instead of the id.
    hostel = serializers.SlugRelatedField(
        queryset=Hostel.objects.all(), slug_field='name')
    room_number = serializers.SlugRelatedField(
        queryset=Rooms.objects.all(), slug_field='name'
    )
    parent = serializers.SlugRelatedField(
        queryset=Parent.objects.all(), slug_field='name'
    )
    guardian = serializers.SlugRelatedField(
        queryset=Guardian.objects.all(), slug_field='name'
    )

    class Meta:
        model = Student
        fields = ('id',
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


                  )
        read_only_field = ['id']
