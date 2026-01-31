import geeassist as gas

# Example 6: Tmap Choropleth with Palette
gas.graphics.tmap_map(
    data="path/to/yield_data.shp",
    col_name="yield_kg",
    title="Agricultural Yield",
    palette="YlOrRd",
    output_file="example_06_tmap_choropleth.jpg"
)
