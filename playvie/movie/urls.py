from django.urls import path, include
from movie.views import get_movies_view, get_genres_view, PlaylistViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('playlists', PlaylistViewSet, basename='playlist')

urlpatterns = [
    path('', include(router.urls)),
    path('', get_movies_view, name='movies_api'),
    path('genres', get_genres_view, name='genres_api')
]