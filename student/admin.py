from django.contrib import admin
from .models import student, category, parent, guardian

admin.site.register(student.Student)
admin.site.register(category.Category)
admin.site.register(parent.Parent)
admin.site.register(guardian.Guardian)
