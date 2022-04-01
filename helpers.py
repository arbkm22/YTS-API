import requests

from models import MovieDetail, MovieList

def get_movie(id: int) -> MovieDetail:
    url = f"https://yts.mx/api/v2/movie_details.json?movie_id={id}&with_images=true&with_cast=true"
    response = requests.get(url)
    if (response.status_code == 200):
        movie = response.json()["data"]["movie"]
        movie_detail = MovieDetail(
            id = movie["id"],
            url = movie["url"],
            imdb_code = movie["imdb_code"],
            title_eng = movie["title_english"],
            year = movie["year"],
            rating = movie["rating"],
            genres = movie["genres"],
            large_cover_image = movie["large_cover_image"],
            download_count = movie["download_count"],
            like_count = movie["like_count"],
            cast = movie["cast"],
            runtime = movie["runtime"],
            description = movie["description"],
            yt_trailer_code = movie["yt_trailer_code"],
            background_image_original = movie["background_image_original"],
            lsi1 = movie["large_screenshot_image1"],
            lsi2 = movie["large_screenshot_image2"],
            lsi3 = movie["large_screenshot_image3"],
            torrents = movie["torrents"]
        )
        return movie_detail
    else:
        print("error")

def get_movie_list() -> MovieList:
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
                genres = movie["genres"],
                large_cover_image = movie["large_cover_image"]
            )
            movies.append(movie_data)
            return movie_data
    else:
        print("error")
    
    movies = []
