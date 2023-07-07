from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination

from movie.api.themoviedb_api import get_genre_data, get_movie_data
from movie.serializers.api_serializers import GenreSerializer, MovieSerializer
from movie.models import Genre, Movie

from playvie.CONSTANTS import BASE_URL_MOVIE_POSTER, API_KEY, GENRE_IDS


@api_view(["GET", "POST"])
def get_movies_view(request):
    #to use the pagination featue in the response
    paginator = PageNumberPagination()
    paginator.page_size = 10
    
    if request.method == 'GET':
        movies = Movie.objects.all().order_by('id')
        
        if movies:
            #To add the paginaton to the results
            paginated_queryset = paginator.paginate_queryset(movies, request)
            movies_serialized = MovieSerializer(paginated_queryset, many=True)
            #Return the JSON list of movies gathered from the DB
            return Response(movies_serialized.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    #In case the request method is POST, the code evaluates if the URL contains the 'page' query parameter to know which data will be retrieved from the external API
    page = request.query_params.get('page')
    if page:
        #First the data from the external API is retrieved.
        api_data = get_movie_data(API_KEY, page)
        if api_data:
            movies_created = 0
            movie_failures = 0
            for movie in api_data['results']:
                try:
                    Movie.objects.get(title=movie['title'])
                    pass
                except Movie.DoesNotExist:
                    #The data is processed and stored only if the movie does not exist in the current DB
                    try:
                        #The data is processed to get only the desired fields and values
                        movie_genre = GENRE_IDS[movie['genre_ids'][0]]
                        movie_genre = Genre.objects.get(name=movie_genre)
                        movie_to_save = {
                            'title': movie['title'],
                            'overview': movie['overview'],
                            'genre': movie_genre.id,
                            'poster': BASE_URL_MOVIE_POSTER + movie['poster_path'],
                            'release': movie['release_date'],
                            'language': movie['original_language'],
                            'adult': movie['adult'],
                            'rate': movie['vote_average'],
                            'votes': movie['vote_count']
                        }
                    except Exception as e:
                        #Raise an error in case the genre of the movie does not exist in the DB
                        print(f'An error ocurred when trying to format the data of the movie [{movie["title"]}]:  {str(e)}')
                        movie_failures += 1
                        continue
                    #The movie data is passed to the serializer to be validated and finally saved in the DB
                    movie_serialized = MovieSerializer(data=movie_to_save)
                    if movie_serialized.is_valid():
                        movie_serialized.save()
                        movies_created += 1
                    else:
                        return Response({'movie': f'{movie_to_save["title"]}',
                                            'errors': movie_serialized.errors}, status=status.HTTP_400_BAD_REQUEST)
            #Confirmation message in case all the for cycle could be executed correctly
            if movies_created:
                response_status = status.HTTP_201_CREATED
            else:
                response_status = status.HTTP_200_OK
                
            return Response({'message': f'{movies_created} total movies created correctly.',
                             'errors': f'{movie_failures}',
                             }, status=response_status)  
        #Error raised in case no data is retrieved from the API
        return Response({"error":"An error was found using the API"},
                        status=status.HTTP_400_BAD_REQUEST)
    return Response({"error":"No any page number was provided as query parameter. It is needed to know which subset of data will be retrieved. Check the API documentation for further information."},
                        status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def get_movie_detail(request, pk=None):
    movie = Movie.objects.get(id=pk)
    if movie:
        if request.method == 'GET':
            movie_serialized = MovieSerializer(movie)
            return Response(movie_serialized.data, status=status.HTTP_200_OK)
        
        #In case the request is PUT type
        movie_serialized = MovieSerializer(instance=movie, data=request.data)        
        if movie_serialized.is_valid():
            movie_serialized.save()
            return Response(movie_serialized.data, status=status.HTTP_200_OK)
        return Response(movie_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'error': "The movie doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET", "POST"])
def get_genres_view(request):
    #to use the pagination featue in the response
    paginator = PageNumberPagination()
    paginator.page_size = 10
    
    data = get_genre_data(API_KEY)
    
    if data:
        if request.method == 'GET':
            genres = Genre.objects.all().order_by('id')
            
            if genres:
                #To add the paginaton to the results
                paginated_queryset = paginator.paginate_queryset(genres, request)
                genres_serialized = GenreSerializer(paginated_queryset, many=True)
                #Return the JSON list of genres gathered from the DB
                return Response(genres_serialized.data, status=status.HTTP_200_OK)
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'POST':
            #Control variable to know the total number of genres saved correctly
            genres_created = 0
            for genre in data['genres']:
                #A try statement to avoid duplicates in the DB
                try:
                    Genre.objects.get(name=genre['name'])
                    continue
                except Genre.DoesNotExist:
                    #the key-value pair 'id' is deleted due to a new ID is generated automatically when the record is created     
                    del genre['id']
                    #The serializer is created with the data as parameter.
                    genre_serializer = GenreSerializer(data=genre)
                    #Only if the data is succesfully validated the record is saved in the DB
                    if genre_serializer.is_valid():
                        genre_serializer.save()
                        genres_created += 1
                    else:
                        return Response(genre_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            #A confirmation message with a 201 code is returned after the for bucle is finished correctly and only if any new genre is created
            if genres_created:
                response_status = status.HTTP_201_CREATED
            else:
                response_status = status.HTTP_200_OK
            
            return Response({'message': f'{genres_created} total genres created',
                             }, response_status)
            
                
    #In case no data is returned by the API, an error is raised.    
    return Response({"error":"An error was found using the API"},
                    status=status.HTTP_400_BAD_REQUEST)       