import requests

 
base_url = url = 'https://api.themoviedb.org/3'

def get_genre_data(api_key):
    endpoint = '/genre/movie/list'
    url = base_url + endpoint + f'?api_key={api_key}'    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_movie_data(api_key, page=None):
    endpoint = '/movie/popular'
    url = base_url + endpoint + f'?api_key={api_key}'
    
    if page:
        url = url + f'&page={page}'
          
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None