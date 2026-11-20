import pandas as pd

df = pd.read_excel("data/raw/tuik_aycicegi_ilce.xls", header=None, engine="calamine")
print(df.iloc[1, 3:8].tolist())     # soru 1
print(df.iloc[4:13, 2].tolist())    # soru 2
print(df[1].dropna())               # soru 3
print(df.shape[1] - 3)              # soru 4