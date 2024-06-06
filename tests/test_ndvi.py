import ee
from geecalcs import NDVI

ee.Initialize()

image = ee.Image([1,2]).rename(['B8', 'B4'])


def test_compute_ndvi():
    ndvi = NDVI('B8', 'B4').compute(image=image)
    assert ndvi.bandNames().getInfo() == ['NDVI']


def test_add_ndvi():
    ndvi = NDVI('B8', 'B4').add(image=image)
    assert ndvi.bandNames().getInfo() == ['B8', 'B4', 'NDVI']


def test_map_ndvi():
    ndvi = NDVI('B8', 'B4')
    collection = ee.ImageCollection([image for _ in range(1, 4)]).map(ndvi)
    assert collection.first().bandNames().getInfo() == ['B8', 'B4', 'NDVI']
