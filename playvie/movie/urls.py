from django.urls import path, include
from movie.views import get_movies_view, get_movie_detail, get_genres_view

from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('', get_movies_view, name='movies'),
    path('<int:pk>', get_movie_detail, name='movie_detail'),
    path('genres', get_genres_view, name='genres')
]