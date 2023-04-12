from django.db import models

from movie.models import Movie


class Playlist(models.Model):
    name = models.CharField(max_length=50, blank=False)
    movies = models.ManyToManyField(Movie)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'playlist'