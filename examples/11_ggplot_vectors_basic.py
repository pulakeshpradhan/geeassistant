import geeassist as gas

# Example 1: Basic Vector Map with ggplot2
# Uses default styling (lightblue fill, black borders)
gas.graphics.ggplot_map(
    data="path/to/districts.shp",
    title="Basic Map of Districts",
    output_file="example_01_basic.jpg"
)
