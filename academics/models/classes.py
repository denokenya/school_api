from django.db import models
from sections import Section

# Create your models here.


class Classes(models.Model):

    """Classes Model which is used to class information ."""

    name = models.CharField(max_length=50, unique=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "classes"
        ordering = ["name"]
        verbose_name = "class"
        verbose_name_plural = "classes"
