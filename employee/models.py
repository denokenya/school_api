from django.db import models
from django.contrib.auth.models import AbstractUser, User
from datetime import datetime
from django.utils import timezone


#from ckeditor.fields import RichTextField


FACULTY = "Faculty"
ACCOUNTANT = "Accountant"
ADMIN = "Admin"
RECEPTIONIST = "Receptionist"
PRINCIPAL = "Principal"
DIRECTOR = "Director"
TECHNICAL_HEAD = "Technical Head"
ACADEMIC = "Academic"
LIBRARY = "Library"
SPORTS = "Sports"
SCIENCE = "Science"
COMMERCE = "Commerce"
ARTS = "Arts"
EXAM = "Exam"
FINANCE = "Finance"
TEACHER = "Teacher"
LIBRARIAN = "Librarian"
SUPER_ADMIN = "Super Admin"
MALE = "Male"
FEMALE = "Female"
SINGLE = "Single"
MARRIED = "Married"
WIDOWED = "Widowed"
SEPARATED = "Separated"
NOT_SPECIFIED = "Not Specified"

# ***************Designation*******************
# _____________________________________________
DESIGNATION = (
    (FACULTY, "Faculty"),
    (ACCOUNTANT, "Accountant"),
    (ADMIN, "Admin"),
    (RECEPTIONIST, "Receptionist"),
    (DIRECTOR, "Director"),
    (TECHNICAL_HEAD, "Technical Head"),

)
# ***************Department*******************
# _____________________________________________


DEPARTMENT = (
    (ACADEMIC, "Academic"),
    (LIBRARY, "Library"),
    (SPORTS, "Sports"),
    (SCIENCE, "Science"),
    (COMMERCE, "Commerce"),
    (ARTS, "Arts"),
    (EXAM, "Exam"),
    (ADMIN, "Admin"),
    (FINANCE, "Finance"),

)


ROLE = (
    (ADMIN, "Admin"),
    (TEACHER, "Teacher"),
    (ACCOUNTANT, "Accountant"),
    (LIBRARIAN, "Librarian"),
    (RECEPTIONIST, "Receptionist"),
    (SUPER_ADMIN, "Superadmin"),
)


GENDER = (

    (MALE, "Male"),
    (FEMALE, "Female"),
)

# ***************MARITAL STATUS*******************
# _____________________________________________

MARITAL_STATUS = (
    (SINGLE, "Single"),
    (MARRIED, "Married"),
    (WIDOWED, "Widowed"),
    (SEPARATED, "Separated"),
    (NOT_SPECIFIED, "Not Specified")


)

# ***************Designation model*******************
# _____________________________________________


class Designation(models.Model):

    """Designation Model which is used to store designation name and date when the role was created ."""

    name = models.CharField(max_length=50, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "designations"
        ordering = ["name"]
        verbose_name = "designation"
        verbose_name_plural = "designations"

# ***************Department model*******************
# _____________________________________________


class Department(models.Model):

    """Department Model which is used to store department name and date when the role was created ."""
    name = models.CharField(max_length=50, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "departments"
        ordering = ["name"]
        verbose_name = "department"
        verbose_name_plural = "departments"

# ***************Designation model*******************
# _____________________________________________


class Role(models.Model):
    """Role Model which is used to store role name and date when the role was created ."""
    name = models.CharField(max_length=50, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "roles"
        ordering = ["name"]
        verbose_name = "role"
        verbose_name_plural = "roles"

# ***************Employee model*******************
# _____________________________________________


class Employee (models.Model):
    """Employee Model"""
    employeeID = models.CharField("Employee ID",
                                  max_length=50, null=False, blank=False, unique=True)
    role = models.ForeignKey(
        Role,  on_delete=models.CASCADE)
    designation = models.ForeignKey(
        Designation,  on_delete=models.CASCADE)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE)
    employeeFirstName = models.CharField("First Name",
                                         max_length=60, blank=False, null=False, default='name')
    employeeLastName = models.CharField("Last Name",
                                        max_length=60, blank=False, null=False, default='name')
    employeeFatherName = models.CharField("Father Name",
                                          max_length=60, blank=True, null=True, default='name')
    employeeEmail = models.EmailField("Email",
                                      null=False, blank=False, unique=True, default='de@gmail.com')
    employeeGender = models.CharField("Gender",
                                      choices=GENDER, max_length=10, blank=False, default=MALE)
    employeeDateOfBirth = models.DateField("Date Of Birth",
                                           null=True, blank=True, default='1900-01-01')
    employeeDateOfJoining = models.DateTimeField(
        "Date Of Joining", null=True, blank=True)

    employeePhone = models.CharField("Mobile Number",
                                     max_length=17, null=False, blank=False, unique=True, default='0711210516')
    employeeEmergencyContactNumber = models.CharField("Emergency Contact Number",
                                                      max_length=17, null=False, blank=True, default='11111111')
    employeeMaritialStatus = models.CharField("Maritial Status",
                                              choices=MARITAL_STATUS, max_length=200, blank=True, default=SINGLE)
    employeeCurrentAddress = models.TextField("Current Address",
                                              max_length=300, null=True, blank=True)
    employeeParmanentAddress = models.TextField("Parmanent Address",
                                                max_length=300, null=True, blank=True)
    employeeQualification = models.TextField("Qualification",
                                             max_length=300, null=True, blank=True)
    employeeWorkExperience = models.TextField("Work Experience",
                                              max_length=300, null=True, blank=True)
    employeeNote = models.CharField(
        "Note", max_length=300, null=True, blank=True)
    is_active = models.BooleanField("Active", default=False)

    def __str__(self):
        return self.employeeFirstName

    class Meta:
        db_table = 'employees'
        ordering = ["role"]
        verbose_name = "employee"
        verbose_name_plural = "employees"
