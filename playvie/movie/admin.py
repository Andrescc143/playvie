from django.contrib import admin

from movie.models import Genre, Movie
from movie.serializers.api_serializers import GenreSerializer, MovieSerializer

admin.site.register(Genre)
admin.site.register(Movie)