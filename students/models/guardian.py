from django.db import models
from datetime import datetime


class Guardian(models.Model):
    """
    This model is used to store the guardian's information of the student.

    """
    name = models.CharField("Guardian Name",
                            max_length=60, blank=True, null=True)

    mobile_phone = models.CharField("Mobile Phone",
                                    max_length=17, null=True, blank=True, unique=True)
    occupation = models.CharField("Guardin Occupation",
                                  max_length=60, blank=True, null=True)
    relation = models.CharField("Guardian Relation",
                                max_length=60, blank=True, null=True)
    email = models.EmailField("Email",
                              null=True, blank=True, unique=True)
    date_created = models.DateField(auto_now_add=True)
    current_address = models.TextField("Current Address",
                                       max_length=300, null=True, blank=True)
    parmanent_address = models.TextField("Parmanent Address",
                                         max_length=300, null=True, blank=True)

    def __str__(self):
        return self.father_name

    class Meta:
        db_table = "guardian"
        ordering = ["name"]
        verbose_name = "guardian"
        verbose_name_plural = "guardians"
