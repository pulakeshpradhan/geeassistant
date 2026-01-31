import geeassistant as gea

# 1. Initialize
gea.init()

# 2. Check info of a simple object
n = gea.get_info(ee.Number(5))
print(f"Number from GEE: {n}")
