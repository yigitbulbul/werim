import ee
ee.Initialize(project="werim-514813")

# --- Things that are the same for every district and year ---
gb_districts = ee.FeatureCollection("WM/geoLab/geoBoundaries/600/ADM2").filter(ee.Filter.eq("shapeGroup", "TUR"))
cropland = ee.ImageCollection("ESA/WorldCover/v200").first().select("Map").eq(40)

def mask_clouds(img):
    scl = img.select("SCL")
    clear = scl.neq(3).And(scl.neq(8)).And(scl.neq(9)).And(scl.neq(10))    # drop cloud shadow and clouds
    return img.updateMask(clear)

def add_ndvi(img):
    return img.normalizedDifference(["B8", "B4"]).rename("NDVI")

# --- One district, one year -> mean July NDVI on cropland + number of images ---
def july_ndvi(gb_name, year):
    district = gb_districts.filter(ee.Filter.eq("shapeName", gb_name)).first().geometry()
    images = (ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
              .filterBounds(district)
              .filterDate(f"{year}-07-01", f"{year}-08-01"))
    ndvi = images.map(mask_clouds).map(add_ndvi).median()
    ndvi_crop = ndvi.updateMask(cropland)
    mean = ndvi_crop.reduceRegion(reducer=ee.Reducer.mean(), geometry=district, scale=10, maxPixels=1e9)
    return mean.getInfo()["NDVI"], images.size().getInfo()

print(july_ndvi("Çorlu", 2023))   # expected: (0.289..., 7)
print(july_ndvi("Çorlu", 2017))   # expected: 3 images
