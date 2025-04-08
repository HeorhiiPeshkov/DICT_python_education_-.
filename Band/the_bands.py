import pytest
from Band.test_band import Band
from Band.generator import Generator

class TestGeneration:
    def test_generate_single(self):
        generator = Generator()
        band = generator.generate_single()
        assert isinstance(band, Band)

    def test_generate_1000(self):
        generator = Generator()
        bands = generator.generate_1000()
        assert isinstance(bands, list)
        assert len(bands) == 1000
        assert all(isinstance(band, Band) for band in bands)

    def test_generate_10_000(self):
        generator = Generator()
        bands = generator.generate_10_000()
        assert isinstance(bands, list)
        assert len(bands) == 10_000
        assert all(isinstance(band, Band) for band in bands)
