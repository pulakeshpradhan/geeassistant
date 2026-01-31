import ee
import geeassistant as gea

gea.init()

l8 = ee.Image('LANDSAT/LC08/C01/T1_TOA/LC08_044034_20140318')

ndvi = gea.indices.calculate_ndvi(l8, 'B5', 'B4', rename='VI')
evi = gea.indices.calculate_evi(l8, 'B5', 'B4', 'B2', rename='VI')

print("Diff calculated.")
