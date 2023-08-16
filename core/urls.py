from django.urls import path,include
from rest_framework.routers import DefaultRouter
from core.views import api 

router = DefaultRouter()
router.register('profile',api.ProfileViewSet,basename="profile")
router.register('users',api.UserViewSet,basename="users")

urlpatterns = [
    path('',include(router.urls)),
]
