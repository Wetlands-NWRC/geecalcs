from abc import ABC, abstractmethod
import ee


class RasterCalculator(ABC):

    def __call__(self, image: ee.Image) -> ee.Image:
        return image.addBands(self.compute(image))

    @abstractmethod
    def compute(self, image: ee.Image):
        """implement the calculation"""
        pass

    def add(self, image: ee.Image) -> ee.Image:
        return image.addBands(self.compute(image))


class NDVI(RasterCalculator):
    def __init__(self, nir: str, red: str, name: str = None) -> None:
        self.nir = nir
        self.red = red
        self.name = name or "NDVI"
        super().__init__()

    def compute(self, image: ee.Image):
        return image.expression(
            expression="(NIR - Red) / (NIR + Red)",
            map_={"NIR": image.select(self.nir), "Red": image.select(self.red)},
        ).rename(self.name)
