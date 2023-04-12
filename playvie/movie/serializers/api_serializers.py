from rest_framework import serializers
from movie.models import Genre, Movie

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
        
        
class MovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        ordering = ['id']
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'title': instance.title,
            'overview': instance.overview,
            'genre': instance.genre.name,
            'poster': instance.poster,
            'release': instance.release,
            'adult': instance.adult,
            'rate': instance.rate,
            'votes': instance.votes
        }