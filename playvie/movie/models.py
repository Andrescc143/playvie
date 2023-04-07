from django.db import models


class Genre(models.Model):  
    name = models.CharField(max_length=25, blank=False)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'genre'

class Movie(models.Model):
    title = models.CharField(max_length=150)
    overview = models.TextField(blank=False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    poster = models.CharField(max_length=120)
    release = models.DateField(auto_now=False, auto_now_add=False)
    language = models.CharField(max_length=15)
    adult = models.BooleanField(blank=True)
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    votes = models.IntegerField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'movie'
