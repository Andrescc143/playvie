from rest_framework import serializers

from movie.models import Playlist


class PlaylistSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Playlist
        ordering = ['id']
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'movies': [movie.title for movie in instance.movies.all()]
        }