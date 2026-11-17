import ee
ee.Initialize(project="werim-514813")
point = ee.Geometry.Point([27.51, 40.98])
collection = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
image = collection.filterBounds(point).filterDate("2025-07-01", "2025-07-31").first()
print(ee.Date(image.get('system:time_start')).format("YYYY-MM-dd").getInfo())