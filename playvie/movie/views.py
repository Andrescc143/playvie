from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from movie.api.themoviedb_api import get_genre_data, get_movie_data
from movie.serializers.api_serializers import GenreSerializer
from movie.models import Genre, Movie


API_KEY = '2212bc4709e02d211e84ffa8614e8c53'

@api_view(["GET"])
def get_movies_view(request, page=None):
    
    data = get_movie_data(API_KEY, page)
    
    if data:
        print(f"Data type: {type(data)}\nData: {data['results'][1]}")
        return Response(data, status=status.HTTP_200_OK)  
        
    return Response({"error":"An error was found using the API"},
                    status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def get_genres_view(request):
    
    data = get_genre_data(API_KEY)
    
    if data:
        if request.method == 'GET':
            #Return the entire JSON list of genres gathered from the API
            return Response(data, status=status.HTTP_200_OK)
        elif request.method == 'POST':
            #Control variable to know the total number of genres saved correctly
            genres_created = 0
            for genre in data['genres']:
                #A try statement to avoid duplicates in the DB
                try:
                    Genre.objects.get(name=genre['name'])
                    pass
                except Genre.DoesNotExist:
                    #the key-value pair 'id' is deleted due to a new ID is generated automatically when the record is created     
                    del genre['id']
                    #The serializer is created with the data as parameter.
                    genre_serializer = GenreSerializer(data=genre)
                    #Only if the data is succesfully validated the record is saved in the DB
                    if genre_serializer.is_valid():
                        genre_serializer.save()
                        genres_created += 1
                        print(f"Genre '{genre['name']}' saved correctly")
                    else:
                        print(f"Error: Genre '{genre['name']}' could not be validated")
                        return Response(genre_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            #A confirmation message an a 201 code is returned after the for bucle is finished correctly
            return Response({'message': f'{genres_created} total genres created correctly',
                             }, status=status.HTTP_201_CREATED)
                
    #In case no data is returned by the API, an error is raised.    
    return Response({"error":"An error was found using the API"},
                    status=status.HTTP_400_BAD_REQUEST)