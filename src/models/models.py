from typing import List, Optional
from pydantic import BaseModel


class Torrents(BaseModel):
    url: str
    hash: str
    quality: str
    type: str
    seeds: int 
    peers: int 
    size: str


class MovieList(BaseModel):
    id: int
    url: str
    imdb_code: str
    title_eng: str
    year: int
    rating: float
    genres: List[str]
    large_cover_image: str


class Cast(BaseModel):
    name: str
    character_name: str
    url_small_image: str
    imdb_code: str


class MovieDetail(MovieList):
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