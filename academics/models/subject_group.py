from django.db import models
from datetime import datetime
# Create your models here.


class Subject_Group(models.Model):

    """Subject Model which is used to store subject information ."""
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, unique=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "subjectgroup"
        ordering = ["name"]
        verbose_name = "subject group"
        verbose_name_plural = "subject groups"
