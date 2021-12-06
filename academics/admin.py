from django.contrib import admin
from .models import classes, sections, subject_group, subjects

admin.site.register(classes.Classes)
admin.site.register(sections.Section)
admin.site.register(subject_group.Subject_Group)
admin.site.register(subjects.Subject)

# Register your models here.
