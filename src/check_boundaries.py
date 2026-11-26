import ee
ee.Initialize(project="werim-514813")
thrace = ee.Geometry.Rectangle([25.9, 40.3, 28.2, 42.2])   # [west, south, east, north]
districts = ee.FeatureCollection("WM/geoLab/geoBoundaries/600/ADM2").filter(ee.Filter.eq("shapeGroup", "TUR")).filterBounds(thrace)
names = districts.aggregate_array("shapeName").getInfo()
print(sorted(names))
print(len(names))