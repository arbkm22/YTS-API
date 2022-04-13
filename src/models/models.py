from dataclasses import dataclass
from typing import List, Optional
from pydantic import BaseModel


class Torrents(BaseModel):
    url: Optional[str]
    hash: Optional[str]
    quality: Optional[str]
    type: Optional[str]
    seeds: Optional[str]
    peers: Optional[str]
    size: Optional[str]

@dataclass
class MovieList():
    #id: int
    #imdb_code: Optional[str]
    url: Optional[str]
    title_eng: Optional[str]
    year: Optional[int]
    #rating: Optional[float]
    #genres: Optional[List[str]]
    #large_cover_image: Optional[str]
    medium_cover_image: Optional[str]

    # def __init__(self, id, url, imdb_code, title_eng, year, 
    #     rating, genres, large_cover_image):
    #     self.id = id
    #     self.url = url
    #     self.imdb_code = imdb_code
    #     self.title_eng = title_eng
    #     self.year = year
    #     self.rating = rating
    #     self.genres = genres
    #     self.large_cover_image = large_cover_image
    #     self.index = dict({
    #         "id": self.id,
    #         "url": self.url,
    #         "imdb_code": self.imdb_code,
    #         "title_eng": self.title_eng,
    #         "year": self.year,
    #         "rating": self.rating,
    #         "genres": self.genres,
    #         "large_cover_image": self.large_cover_image
    #     })
    def __init__(self, url, title_eng, year, medium_cover_image):
        self.url = url
        self.title_eng = title_eng
        self.year = year
        self.medium_cover_image = medium_cover_image
        self.index = dict({
            "title_eng": self.title_eng,
            "year": self.year,
            "medium_cover_image": self.medium_cover_image
        })

    def __getitem__(self, index):
        return self.index[index]

class Cast(BaseModel):
    name: Optional[str]
    character_name: Optional[str]
    url_small_image: Optional[str]
    imdb_code: Optional[str]


class MovieDetail(BaseModel):
    id: int
    url: str
    imdb_code: Optional[str]
    title_eng: Optional[str]
    year: Optional[int]
    rating: Optional[float]
    genres: Optional[List[str]]
    large_cover_image: Optional[str]
    medium_cover_image: Optional[str]
    download_count: Optional[int]
    like_count: Optional[int]
    cast: Optional[List[Cast]]
    runtime: Optional[int]
    description_full: Optional[str]
    yt_trailer_code: Optional[str]
    language: Optional[str]
    background_image_original: Optional[str]
    lsi1: Optional[str]
    lsi2: Optional[str]
    lsi3: Optional[str]
    torrents: List[Torrents]