from django.contrib import admin
from .models import hostel, hostel_rooms, room_type

admin.site.register(hostel_rooms.Rooms)
admin.site.register(hostel.Hostel)
admin.site.register(hostel.Room_Type)

# Register your models here.
