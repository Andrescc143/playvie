from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from playlist.models import Playlist
from playlist.serializers import PlaylistSerializer


class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all().order_by('id')
    serializer_class = PlaylistSerializer
    
    def create(self, request):                     
        serialized_playlist = self.serializer_class(data=request.data)
        
        if serialized_playlist.is_valid():
            serialized_playlist.save()                
            return Response({'message': 'Playlist created correctly', 'data': serialized_playlist.data}, status=status.HTTP_201_CREATED)
        
        return Response(serialized_playlist.errors, status=status.HTTP_400_BAD_REQUEST)