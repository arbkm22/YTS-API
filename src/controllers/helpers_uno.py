from cgitb import reset
import requests
from bs4 import BeautifulSoup

from src.models.models import MovieList

# This module uses web scraping to get the data

def movies_list(url: str) -> MovieList:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    result = soup.find_all("div", class_="browse-movie-wrap col-xs-10 col-sm-4 col-md-5 col-lg-4")
    return_list = []
    for movie in result:
        img = movie.find("img", class_="img-responsive")
        name = movie.find("a", class_="browse-movie-title")
        year = movie.find("div", class_="browse-movie-year")
        title_eng = name.text.strip()
        year = year.text.strip()
        img = img["src"]
        movie_data = MovieList(
            title_eng = title_eng,
            year = year,
            medium_cover_image = img
        )
        return_list.append(movie_data)

    return return_list

def get_latest_movies():
    URL = "https://yts.mx/browse-movies/0/all/all/0/latest/2022/all"
    latest_movies = movies_list(URL)
    return latest_movies

def get_popular_movies():
    URL = "https://yts.mx/browse-movies/0/all/all/0/downloads/2022/all"
    popular_movies = movies_list(URL)
    return popular_movies

def get_most_liked_movies():
    URL = "https://yts.mx/browse-movies/0/all/all/0/likes/0/all"
    most_liked_movies = movies_list(URL)
    return most_liked_movies