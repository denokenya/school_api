from django.contrib import admin
from .models import student, category

admin.site.register(student.Student)
admin.site.register(category.Category)

# Register your models here.
