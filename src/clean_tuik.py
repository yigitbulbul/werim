import pandas as pd

df = pd.read_excel("data/raw/tuik_aycicegi_ilce.xls", header=None, engine="calamine")
districts = df.iloc[1, 3:].tolist()   # row 1, from column 3: district names
years = df.iloc[22:31, 2].tolist()    # column 2, rows 22–30: years

yield_block = df.iloc[22:31, 3:]      # the numbers
print(yield_block.shape)

yield_block.columns = districts    # name the columns with district names
yield_block.index = years          # name the rows with years

long = yield_block.reset_index().melt(id_vars="index", var_name="district", value_name="yield_kg_da")
long = long.rename(columns={"index": "year"})   # rename a column: {"old": "new"}
long["year"] = long["year"].astype(int)          # convert to whole numbers
parts = long["district"].str.extract(r"(.+)\((.+)\)-(\d+)")
long["province"] = parts[0]
long["district"] = parts[1]
long["code"] = parts[2]
print(long.head())
print(long.shape)   