from django.db import models
import hostel
from hostel.models.hostel import Hostel


class Rooms(models.Model):
    """
        Model containing hostel rooms information
    """
    name = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    number_of_rooms = models.IntegerField()

    class Meta:
        db_table = "hostel-rooms"
        ordering = ["name"]
        verbose_name = "hostel room"
        verbose_name_plural = "hostel rooms"
