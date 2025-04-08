import random
from Band.test_band import Band  # Импортируем класс Band

class Generator:
    band_names = ['Sonic Youth', 'Jethro Tull', 'Rainbow', 'Bauhaus', 'Nick Cave & The Bad Seeds']
    band_countries = ['USA', 'Great Britain', 'USA', 'Great Britain', 'Germany']
    band_genres = ['Noise rock', 'Progressive folk', 'Progressive hard rock', 'Gothic rock', 'Punk blues']

    def generate_single(self) -> Band:
        band_name = random.choice(self.band_names)
        band_albums = random.randint(4, 20)
        band_country = random.choice(self.band_countries)
        band_genre = random.choice(self.band_genres)
        band_existing = random.randint(45, 57)
        return Band(band_name, band_genre, band_country, band_albums, band_existing)

    def generate_1000(self) -> list:
        return [self.generate_single() for _ in range(1000)]

    def generate_10_000(self) -> list:
        return [self.generate_single() for _ in range(10_000)]
