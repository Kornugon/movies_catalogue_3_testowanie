import requests
import random

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhZTQxNDVhYWZmYTQ4MDQ5ODRkYTRlNDU2ODY1Y2IxNyIsInN1YiI6IjVmZjdiMWI4OTFmMGVhMDAzZjkyOTc2NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.y8xBRnexLAYN_tyO7lnXMHExTcoAs2LcJXj4XKcxIj8"


def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {API_TOKEN}"
   }
   response = requests.get(full_url, headers=headers)
   response.raise_for_status()
   return response.json()


def get_popular_movies():
   return call_tmdb_api(f"movie/popular")

def get_movies_list(list_type="popular"):
   return call_tmdb_api(f"movie/{list_type}")

def get_single_movie(movie_id):
   return call_tmdb_api(f"movie/{movie_id}")

def get_single_movie_cast(movie_id):
   return call_tmdb_api(f"movie/{movie_id}/credits")["cast"]

def get_movie_images(movie_id):
   return call_tmdb_api(f"movie/{movie_id}/images")



def generate_random_movies(list_type):
    """
    Randomise Popular Movies
    """
    data = []
    movies = get_movies_list(list_type)["results"]

    for _ in range(len(movies)):
        show = random.choice(movies)
        if show not in data:
            data.append(show)
    return data


def get_movies(how_many, list_type):
    """
    Generate random movies from popular type.
    For others types there is no randomise.
    """
    if list_type == "popular":
        data = generate_random_movies(list_type)
    else:
        data = get_movies_list(list_type)["results"]
    return data[:how_many]


def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"
