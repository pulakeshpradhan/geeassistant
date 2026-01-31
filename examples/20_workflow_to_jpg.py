import geeassist as gas
from geeassist.workflows import auto_process_and_map

# Example 10: Full Workflow to JPG
# This single call:
# 1. Finds 'Kolkata' boundary via FAO GAUL
# 2. Computes NDVI from Sentinel-2
# 3. Downloads as .tif
# 4. Generates a publication-quality .jpg map
auto_process_and_map(
    location_name="Kolkata",
    start_date="2023-01-01",
    end_date="2023-01-31",
    output_dir="kolkata_final",
    use_ggplot=True
)
