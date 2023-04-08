from django.contrib import admin

from movie.models import Genre, Movie, Playlist
from movie.serializers.api_serializers import GenreSerializer, MovieSerializer

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Playlist)