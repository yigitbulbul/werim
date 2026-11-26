import ee
ee.Initialize(project="werim-514813")
gb_districts = ee.FeatureCollection("WM/geoLab/geoBoundaries/600/ADM2").filter(ee.Filter.eq("shapeGroup", "TUR"))

corlu = gb_districts.filter(ee.Filter.eq("shapeName", "Çorlu")).first().geometry()
images = (ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
          .filterBounds(corlu)
          .filterDate("2023-07-01", "2023-08-01"))
def mask_clouds(img):
    scl = img.select("SCL")
    clear = scl.neq(3).And(scl.neq(8)).And(scl.neq(9)).And(scl.neq(10))    # drop cloud shadow and clouds
    return img.updateMask(clear)
def add_ndvi(img):
    return img.normalizedDifference(["B8", "B4"]).rename("NDVI")
ndvi = images.map(mask_clouds).map(add_ndvi).median()
cropland = ee.ImageCollection("ESA/WorldCover/v200").first().select("Map").eq(40)
ndvi_crop = ndvi.updateMask(cropland)
mean = ndvi_crop.reduceRegion(reducer=ee.Reducer.mean(), geometry=corlu, scale=10, maxPixels=1e9)
print(mean.getInfo())
print(images.size().getInfo())