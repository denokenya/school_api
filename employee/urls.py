from . views import DesignationViewSet, DepartmentViewSet, RoleViewSet, EmployeeViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register("employee_designation", DesignationViewSet, "designations")
router.register("employee_department", DepartmentViewSet, "departments")
router.register("employee_role", RoleViewSet, "roles")
router.register("employee", EmployeeViewSet, "employees")


#urlpatterns = router.urls
urlpatterns = [
    path('api/token', obtain_auth_token, name='api-token'),
    path('api/', include(router.urls)),
]
