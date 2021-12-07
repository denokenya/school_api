from django.db import router


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


from hostel.api.views.room_type_view import Room_Type_ViewSet
from hostel.api.views.hostel_view import Hostel_ViewSet

router = DefaultRouter()
router.register("hostel_room_type", Room_Type_ViewSet, "hostel_room_type")
router.register("hostel", Hostel_ViewSet, "hostel")

urlpatterns = [
    path('api/token', obtain_auth_token, name='api-token'),
    path('', include(router.urls)),
]
