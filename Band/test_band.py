import pytest
from Band.the_bands import Band


class Band:
    def __init__(self, name, genres, country, total_studio_albums, age):
        self.name = name
        self.genres = genres
        self.country = country
        self.total_studio_albums = total_studio_albums
        self.age = age


class TestBand(Band):
    def test_band(self):
        band =  Band('Sonic Youth', 'Noise rock', 'USA', 20, 31)
        assert isinstance(band, Band)


    def test_band_init(self):
        band = Band('Sonic Youth', 'Noise rock', 'USA', 20, 31)
        assert band.name == 'Sonic Youth'
        assert band.genres == 'Noise rock'
        assert band.country == 'USA'
        assert band.total_studio_albums == 20
        assert band.age == 31


    def test_get_info(self):
        band = Band('Sonic Youth', 'Noise rock', 'USA', 20, 31)
        expected = 'Band(Sonic Youth, Noise rock, USA, 20, 31)'


    def get_info(self) -> str:
        return f'Band({self.name}, {self.genres}, {self.country}, {self.total_studio_albums}, {self.age})'

