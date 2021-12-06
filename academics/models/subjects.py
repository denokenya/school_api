from django.db import models
from subject_group import Subject_Group
from classes import Classes
# Create your models here.


class Subject(models.Model):

    """Subject Model which is used to store subject information ."""
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50, unique=True)
    subject_class = models.ForeignKey(Classes, on_delete=models.CASCADE)
    group = models.ForeignKey(Subject_Group, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "subject"
        ordering = ["name"]
        verbose_name = "subject"
        verbose_name_plural = "subjects"
