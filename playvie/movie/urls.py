from django.urls import path
from movie.views import get_movies_view, get_genres_view


urlpatterns = [
    path('source/', get_movies_view, name='movies_api'),
    path('source/<int:page>', get_movies_view, name='movies_api'),
    path('source/genres', get_genres_view, name='genres_api')
]