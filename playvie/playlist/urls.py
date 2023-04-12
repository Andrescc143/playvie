from django.urls import path, include
from playlist.views import PlaylistViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', PlaylistViewSet, basename='playlist')

urlpatterns = [
    path('', include(router.urls))
]