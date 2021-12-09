from django.db import models
from datetime import datetime


class Parent(models.Model):
    """
    This model is used to store the parent's information of the student.

    """
    father_name = models.CharField("Father Name",
                                   max_length=60, blank=True, null=True)

    father_phone = models.CharField("Father Phone",
                                    max_length=17, null=True, blank=True, unique=True)
    father_occupation = models.CharField("Father Occupation",
                                         max_length=60, blank=True, null=True)
    mother_name = models.CharField("Mother Name",
                                   max_length=60, blank=True, null=True)

    mother_phone = models.CharField("Mother Phone",
                                    max_length=17, null=True, blank=True, unique=True)
    mother_occupation = models.CharField("Mother Occupation",
                                         max_length=60, blank=True, null=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.father_name

    class Meta:
        db_table = "parent"
        ordering = ["father_name"]
        verbose_name = "parent"
        verbose_name_plural = "parents"
