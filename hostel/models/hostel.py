from django.db import models
from hostel.models.room_type import Room_Type
from .room_type import Room_Type
from datetime import datetime


class Hostel(models.Model):
    """
        Model containing hostel information
    """
    name = models.CharField(max_length=50, unique=True)
    room_type = models.ForeignKey(Room_Type, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "hostel"
        ordering = ["name"]
        verbose_name = "hostel"
        verbose_name_plural = "hostels"
