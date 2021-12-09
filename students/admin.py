from django.contrib import admin
from .models.category import Category
from .models.guardian import Guardian
from .models.parent import Parent
from .models.student import Student

admin.site.register(Category)
admin.site.register(Guardian)
admin.site.register(Parent)
admin.site.register(Student)
