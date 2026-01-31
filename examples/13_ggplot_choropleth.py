import geeassist as gas

# Example 3: Choropleth Map with ggplot2
# Maps a specific column (e.g., 'population') to color
gas.graphics.ggplot_map(
    data="path/to/census_data.shp",
    col_name="population",
    title="Population Distribution",
    output_file="example_03_choropleth.jpg"
)
