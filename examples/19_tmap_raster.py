import geeassist as gas

# Example 9: Raster Thematic Map with tmap
# Uses the 'RdYlGn' palette commonly used for vegetation
gas.graphics.tmap_raster_map(
    raster_path="path/to/ndvi.tif",
    title="NDVI Thematic Map (tmap)",
    output_file="example_09_raster_tmap.jpg"
)
