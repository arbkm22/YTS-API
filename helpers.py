import requests

from models import MovieList

def get_movie_list():
    url = "https://yts.mx/api/v2/list_movies.json"
    response = requests.get(url)
    if (response.status_code == 200):
        data = response.json()["data"]["movies"]
        movies = []
        for movie in data:
            movie_data = MovieList(
                id = movie["id"],
                url = movie["url"],
                imdb_code = movie["imdb_code"],
                title_eng = movie["title_english"],
                year = movie["year"],
                rating = movie["rating"],
                runtime = movie["runtime"],
                genres = movie["genres"],
                summary = movie["summary"],
                yt_trailer_code = movie["yt_trailer_code"],
                language = movie["language"],
                mpa_rating = movie["mpa_rating"],
                background_image_original = movie["background_image_original"],
                medium_cover_image = movie["medium_cover_image"],
                large_cover_image = movie["large_cover_image"],
                torrents = movie["torrents"]

            )
            movies.append(movie_data)
            return movie_data
    else:
        print("error")
    
    movies = []
