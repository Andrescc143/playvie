from rest_framework import serializers

from movie.models import Playlist


class PlaylistSerializer(serializers.ModelSerializer):
    #movies = serializers.StringRelatedField()
    
    class Meta:
        model = Playlist
        ordering = ['id']
        fields = '__all__'