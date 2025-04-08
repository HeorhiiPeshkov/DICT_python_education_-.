from abc import ABC, abstractmethod


class AbstractMusicBandCollection(ABC):
    @abstractmethod
    def append(self, band):
        pass
    @abstractmethod
    def insert(self, index, band):
        pass
    @abstractmethod
    def index(self, name, start=0, stop=None):
        pass
    @abstractmethod
    def remove(self, name):
        pass
    @abstractmethod
    def __getitem__(self, index):
        pass
    @abstractmethod
    def __setitem__(self, index, band):
        pass
    @abstractmethod
    def __len__(self):
        pass
    @abstractmethod
    def __repr__(self):
        pass


class MusicBand:
    def __init__(self, name, genre, country, total_studio_albums, age):
        self.name = name
        self.genre = genre
        self.country = country
        self.total_studio_albums = total_studio_albums
        self.age = age
    def __repr__(self):
        return f'MusicBand({self.name}, {self.genre}, {self.country}, {self.total_studio_albums}, {self.age}'


class BasicMusicBandCollection(AbstractMusicBandCollection):
    def __init__(self, bands=None):
        self.bands = bands if bands else []
    def __len__(self):
        return len(self.bands)
    def __repr__(self):
        return f'BasicMusicBandCollection({self.bands})'
    def __getitem__(self, index):
        return self.bands[index]
    def __setitem__(self, index, band):
        self.bands[index] = band
    def append(self, band):
        self.bands.append(band)
    def insert(self, index, band):
        self.bands.insert(index, band)
    def index(self, name, start=0, stop=None):
        stop = stop if stop else len(self.bands)
        for i in range(start, stop):
            if self.bands[i].name == name:
                return i
        raise ValueError('MusicBand not found')
    def remove(self, name):
        index = self.index(name)
        del self.bands[index]


class UniqueMusicBandCollection(BasicMusicBandCollection):
    def append(self, band):
        if band not in self.bands:
            super().append(band)
    def insert(self, index, band):
        if band not in self.bands:
            super().insert(index, band)


class SortedMusicBandCollection(BasicMusicBandCollection):
    def append(self, band):
        super().append(band)
        self.bands.sort(key=lambda b: b.name)
    def insert(self, index, band):
        super().append(band)
        self.bands.sort(key=lambda b: b.name)
    def __setstate__(self, index, band):
        super().__setitem__(index, band)
        self.bands.sort(key=lambda b: b.name)

band1 = MusicBand('Einsturzende Neubauten', 'Industrial', 'German', 25, 45)
band2 = MusicBand('Mitski', 'Noise Pop', 'USA', 7, 13)
band3 = MusicBand('True Widow', 'Post Rock', 'USA', 4, 18)
basic_collection = BasicMusicBandCollection([band1, band2])
print(len(basic_collection))










