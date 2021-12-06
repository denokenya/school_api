from django.db import models
from academics.models import(
    classes,
    sections)
from .category import Category

from constants import constants
from hostel.models import hostel
from datetime import datetime

FEMALE = "Female"
MALE = "Male"
GENDER = "Gender"
GENDER = (
    (MALE, "Male"),
    (FEMALE, "Female"),
)

RELIGION = (
    (constants.CHRISTIAN, "Christian"),
    (constants.MUSLIM, "Muslim"),
    (constants.HINDU, "Hindu"),
    (constants.OTHER, "Other"),
)


class Student(models.Model):

    """
        Student model which is used to capture student admission
        details.

    """
    admission_no = models.CharField("Admission No",
                                    max_length=50, null=False, blank=False, unique=True)
    roll_no = models.CharField("Roll No",
                               max_length=50, null=False, blank=False, unique=True)
    student_class = models.ForeignKey(
        classes.Classes, on_delete=models.CASCADE)
    section = models.ForeignKey(sections.Section, on_delete=models.CASCADE)
    first_name = models.CharField("First Name",
                                  max_length=60, blank=False, null=False, default='name')
    last_name = models.CharField("First Name",
                                 max_length=60, blank=False, null=False, default='name')
    gender = models.CharField("Gender",
                              choices=GENDER, max_length=10, blank=False, default=MALE)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    religion = models.CharField("Religion",
                                choices=RELIGION, max_length=10, blank=False, default=constants.CHRISTIAN)
    mobile_number = models.CharField("Mobile Number",
                                     max_length=17, null=False, blank=True, unique=True)
    email = models.EmailField("Email",
                              null=False, blank=False, unique=True)
    admission_date = models.DateTimeField(
        "Admission Date", null=True, blank=True)
    blood_group = models.CharField("Blood Group",
                                   max_length=2, blank=True, null=True)
    hostel = models.ForeignKey(hostel.Hostel, on_delete=models.CASCADE)
    height = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)
    medical_history = models.TextField("Medical History",
                                       max_length=300, null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        db_table = "student"
        ordering = ["admission_no"]
        verbose_name = "student"
        verbose_name_plural = "student"
