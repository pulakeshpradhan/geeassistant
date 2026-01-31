import ee
import geeassistant as gea
from geeassistant.workflows import get_fao_gaul

gea.init()

# Get geometry for Kolkata
kolkata_geom = get_fao_gaul("Kolkata", level=2)

print("Kolkata Geometry found.")
info = kolkata_geom.getInfo()
print(f"Type: {info['type']}")
