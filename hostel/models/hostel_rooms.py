from django.db import models
import hostel
from hostel.models.hostel import Hostel


class Rooms(models.Model):
    """
        The Model containing hostel rooms information
    """
    name = models.ForeignKey(
        Hostel, related_name='hostels', on_delete=models.CASCADE)
    room_number = models.CharField("Room Number",
                                   max_length=10, null=True, blank=True, unique=True)

    def __str__(self):
        return self.room_number

    class Meta:
        db_table = "hostel-rooms"
        ordering = ["name"]
        verbose_name = "hostel room"
        verbose_name_plural = "hostel rooms"
