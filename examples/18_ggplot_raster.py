import geeassist as gas

# Example 8: Raster NDVI Map with ggplot2
# Visualizes a GeoTIFF (e.g., exported from GEE)
gas.graphics.ggplot_raster_map(
    raster_path="path/to/ndvi.tif",
    title="NDVI Visualization (ggplot2)",
    output_file="example_08_raster_ggplot.jpg"
)
