from django.db import router


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


from students.api.views.category_view import Category_ViewSet
from students.api.views.guardian_view import Guardian_ViewSet
from students.api.views.parent_view import Parent_ViewSet
from students.api.views.student_view import Student_ViewSet


router = DefaultRouter()

router.register("student_category", Category_ViewSet, "student_category")
router.register("student_guardian", Guardian_ViewSet, "student_guardian")
router.register("student_parent", Parent_ViewSet, "student_parent")
router.register("student", Student_ViewSet, "student")


urlpatterns = [
    path('api/token', obtain_auth_token, name='api-token'),
    path('', include(router.urls)),
]
