import requests

from src.models.models import MovieDetail, MovieList

# This module uses the official api to implement the helper function

def get_movie(id: int) -> MovieDetail:
    url = f"https://yts.mx/api/v2/movie_details.json?movie_id={id}&with_images=true&with_cast=true"
    response = requests.get(url)
    if (response.status_code == 200):
        movie = response.json()["data"]["movie"]
        movie_detail = MovieDetail(
            id = movie.get("id"),
            url = movie.get("url"),
            imdb_code = movie.get("imdb_code"),
            title_eng = movie.get("title_english"),
            year = movie.get("year"),
            rating = movie.get("rating"),
            genres = movie.get("genres"),
            large_cover_image = movie.get("large_cover_image"),
            download_count = movie.get("download_count"),
            like_count = movie.get("like_count"),
            cast = movie.get("cast"),
            runtime = movie.get("runtime"),
            description_full = movie.get("description_full"),
            yt_trailer_code = movie.get("yt_trailer_code"),
            language = movie.get("language"),
            background_image_original = movie.get("background_image_original"),
            lsi1 = movie.get("large_screenshot_image1"),
            lsi2 = movie.get("large_screenshot_image2"),
            lsi3 = movie.get("large_screenshot_image3"),
            torrents = movie.get("torrents")
        )
        return movie_detail
    else:
        print("error")

def get_movie_list(page: int = 1):
    url = f"https://yts.mx/api/v2/list_movies.json?page={page}"
    response = requests.get(url)
    if (response.status_code == 200):
        data = response.json()["data"]["movies"]
        movies = []
        for movie in data:
            movie_data = MovieList(
                id = movie.get("id"),
                url = movie.get("url"),
                imdb_code = movie.get("imdb_code"),
                title_eng = movie.get("title_english"),
                year = movie.get("year"),
                rating = movie.get("rating"),
                genres = movie.get("genres"),
                large_cover_image = movie.get("large_cover_image")
            )
            movies.append(movie_data)
        return movies
    else:
        print("error")
        return []
