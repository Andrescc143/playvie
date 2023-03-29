from django.urls import path
from movie.views import get_movies_view


urlpatterns = [
    path('source', get_movies_view, name='movies_api')
]