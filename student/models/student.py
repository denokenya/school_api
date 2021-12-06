from django.db import models
from academics.models import(
    classes,
    sections)
import category
from employee.models import FEMALE, GENDER, MALE
from student.models.category import Category
from constants import constants

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
