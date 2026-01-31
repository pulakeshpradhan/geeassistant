# User Guide

## Initialization

Before using GEE functionalities, you must initialize the library. `geeassistant` handles the standard `ee.Initialize()` call and can trigger authentication if needed.

```python
import geeassistant as gea

# Simple init
gea.init()

# Init with a specific project
gea.init(project='my-gee-project')
```

## Calculating Indices

One of the most common tasks in remote sensing is calculating spectral indices.

### NDVI

Normalized Difference Vegetation Index (NDVI) is used to quantify vegetation greenness.

```python
import ee
import geeassistant as gea

# Load a Landsat 8 image
image = ee.Image('LANDSAT/LC08/C01/T1_TOA/LC08_044034_20140318')

# Calculate NDVI (B5 is NIR, B4 is Red for Landsat 8)
ndvi_image = gea.indices.calculate_ndvi(image, nir_band='B5', red_band='B4')

# The resulting image has a new band named 'NDVI'
print(ndvi_image.bandNames().getInfo())
```

### NDWI

Normalized Difference Water Index (NDWI) is useful for water body mapping.

```python
# Calculate NDWI (B3 is Green, B5 is NIR for Landsat 8)
ndwi_image = gea.indices.calculate_ndwi(image, green_band='B3', nir_band='B5')
```

## Cloud Masking

`geeassistant` provides helpers to mask clouds.

```python
# Function to mask clouds for Landsat 8
masked_image = gea.utils.mask_clouds_landsat8(image)
```

## Exporting Data

Exporting images to Google Drive is simplified.

```python
# Define a region of interest
geometry = ee.Geometry.Rectangle([77, 12, 78, 13])

# Export
gea.utils.export_image_to_drive(
    image=ndvi_image.select('NDVI'),
    description='ndvi_export_example',
    folder='GEE_Exports',
    region=geometry,
    scale=30
)
```
