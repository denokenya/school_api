from django.db import models
from datetime import datetime


class Room_Type(models.Model):
    """
        Model containing hostel room type information
    """
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "hostel-rooms_type"
        ordering = ["name"]
        verbose_name = "hostel room type"
        verbose_name_plural = "hostel rooms type"
