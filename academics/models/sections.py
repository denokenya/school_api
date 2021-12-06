from django.db import models
from datetime import datetime

# Create your models here.


class Section(models.Model):

    """Section Model which is used to section information ."""

    name = models.CharField(max_length=50, unique=True)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "section"
        ordering = ["name"]
        verbose_name = "section"
        verbose_name_plural = "sections"
