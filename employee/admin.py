from django.contrib import admin
from .models import Employee, Designation, Department, Role

'''Actions to be performed'''


def update_designation(modeladmin, request, queryset):
    queryset.update(role="Admin")


update_designation.short_description = 'Update role'

# sets values for how the admin site lists your designations


class DesignationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']
    list_display_links = ['name']
    list_per_page = 15

# sets values for how the admin site lists your departments


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']
    list_display_links = ['name']
    list_per_page = 15

# sets values for how the admin site lists your roles


class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    ordering = ['name']
    list_display_links = ['name']
    list_per_page = 15
    site_header = "Roles Administration"
    site_header_color = "black"

    admin.site.site_header_color = "green"
    admin.site.module_caption_color = "pink"

# sets values for how the admin site lists your employees


class EmployeeAdmin(admin.ModelAdmin):

    list_display = [
        'employeeID',
        'employeeFirstName',
        'employeeLastName',
        'role',
        'designation',
        'department',
        'employeePhone',
        'employeeEmail',
        'is_active',


    ]
    search_fields = [
        'employeeID',
        'employeeFirstName',
        'employeeLastName',
        'employeePhone',
        'employeeEmail'

    ]
    ordering = ['employeeID']
    list_display_links = [
        'employeeID',
        'employeeFirstName',
        'employeeLastName',
    ]

    list_filter = [
        'role',
        'designation',
        'department',
    ]
    list_per_page = 15
    actions = [update_designation]


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Designation, DesignationAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.site_header_color = "green"
admin.site.module_caption_color = "pink"
