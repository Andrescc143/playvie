from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from movie.api.themoviedb_api import get_genre_data, get_movie_data


API_KEY = '2212bc4709e02d211e84ffa8614e8c53'

@api_view(["GET"])
def get_movies_view(request):
    data = get_movie_data(API_KEY)
    
    if data:
        return Response(data, status=status.HTTP_200_OK)
    return Response({"error":"An error was found using the API"},
                    status=status.HTTP_400_BAD_REQUEST)