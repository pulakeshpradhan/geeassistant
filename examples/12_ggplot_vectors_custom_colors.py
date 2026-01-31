import geeassist as gas

# Example 2: Customized Vector Colors in ggplot2
gas.graphics.ggplot_map(
    data="path/to/districts.shp",
    title="Customized Colors Visualization",
    color="lightgreen",
    edge_color="darkgreen",
    output_file="example_02_custom_colors.jpg"
)
