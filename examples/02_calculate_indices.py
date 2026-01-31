import ee
import geeassistant as gea

gea.init()

# Landsat 8 image
image = ee.Image('LANDSAT/LC08/C01/T1_TOA/LC08_044034_20140318')

# Calculate indices
img_ndvi = gea.indices.calculate_ndvi(image, 'B5', 'B4')
img_ndwi = gea.indices.calculate_ndwi(image, 'B3', 'B5')

print(f"Bands after calc: {img_ndvi.bandNames().getInfo()}")
