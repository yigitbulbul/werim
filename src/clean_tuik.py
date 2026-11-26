import pandas as pd

df = pd.read_excel("data/raw/tuik_aycicegi_ilce.xls", header=None, engine="calamine")
districts = df.iloc[1, 3:].tolist()   # row 1, from column 3: district names
def read_block(start_row, value_name):
    years = df.iloc[start_row:start_row+9, 2].tolist()    # column 2, rows start_row–(start_row+8): years
    yield_block = df.iloc[start_row:start_row+9, 3:]      # the numbers
    yield_block.columns = districts    # name the columns with district names
    yield_block.index = years          # name the rows with years
    long = yield_block.reset_index().melt(id_vars="index", var_name="district", value_name=value_name)
    long = long.rename(columns={"index": "year"})   # rename a column: {"old": "new"}
    long["year"] = long["year"].astype(int)          # convert to whole numbers
    parts = long["district"].str.extract(r"(.+)\((.+)\)-(\d+)")
    long["province"] = parts[0]
    long["district"] = parts[1]
    long["code"] = parts[2]
    return long
test = read_block(4, "sown_area_da")
print(test.head())
print(test.shape)     