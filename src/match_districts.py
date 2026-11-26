import pandas as pd
import ee

ee.Initialize(project="werim-514813")
thrace = ee.Geometry.Rectangle([25.9, 40.3, 28.2, 42.2])   # [west, south, east, north]
gb_districts = ee.FeatureCollection("WM/geoLab/geoBoundaries/600/ADM2").filter(ee.Filter.eq("shapeGroup", "TUR")).filterBounds(thrace)
gb_names = gb_districts.aggregate_array("shapeName").getInfo()

def to_gb_name(province, district):
    if district == "Merkez":
        name = province + " merkez"
    else:
        name = district
    name = name.replace("ş", "?").replace("ı", "?").replace("ğ", "?").replace("İ", "?").replace("Ş", "?")
    return name

tuik = pd.read_csv("data/processed/tuik_yield.csv")
districts = tuik[["province", "district", "code"]].drop_duplicates()
gb_list = []
for _, row in districts.iterrows():
    gb_list.append(to_gb_name(row["province"], row["district"]))
districts["gb_name"] = gb_list
districts["found"] = districts["gb_name"].isin(gb_names)
print(districts[~districts["found"]])
print(districts["found"].sum())
cols = ["code", "province", "district", "gb_name"]
districts[cols].to_csv("data/district_mapping.csv", index=False)
