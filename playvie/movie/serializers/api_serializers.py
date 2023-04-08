from rest_framework import serializers
from movie.models import Genre, Movie

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        
        
class MovieSerializer(serializers.ModelSerializer):
    genre = serializers.StringRelatedField()
    
    class Meta:
        model = Movie
        ordering = ['id']
        fields = '__all__'