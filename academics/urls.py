from django.db import router


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


from academics.api.views.classes_view import Classes_ViewSet
from academics.api.views.sections_view import Section_ViewSet
from academics.api.views.subject_group_view import Subject_Group_ViewSet
from academics.api.views.subject_view import Subject_ViewSet


router = DefaultRouter()
router.register("class", Classes_ViewSet, "classes")
router.register("class_section", Section_ViewSet, "class_section")
router.register("class_subject_group",
                Subject_Group_ViewSet, "class_subject_group")
router.register("class_subject", Subject_ViewSet, "class_subject")


urlpatterns = [
    path('api/token', obtain_auth_token, name='api-token'),
    path('', include(router.urls)),
]
