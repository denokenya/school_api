from django.db import models


class Category(models.Model):

    """Category Model which is used to store student category name and date when the category was created ."""
    name = models.CharField(max_length=50, unique=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "student_category"
        ordering = ["name"]
        verbose_name = " student category"
        verbose_name_plural = " student categories"
