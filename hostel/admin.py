from django.contrib import admin
from .models import hostel, hostel_rooms, room_type


class Hostel_Rooms_Admin(admin.ModelAdmin):

    list_display = [
        'room_number',
        'name',

    ]
    search_fields = [


        'room_number',
    ]
    ordering = ['name']
    list_display_links = [
        'room_number',
    ]

    list_filter = [
        'name',
        'room_number',
    ]
    list_per_page = 15


admin.site.register(hostel_rooms.Rooms, Hostel_Rooms_Admin)
admin.site.register(hostel.Hostel)
admin.site.register(hostel.Room_Type)

# Register your models here.
