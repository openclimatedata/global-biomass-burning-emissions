import pandas as pd

from pandas_datapackage_reader import read_datapackage
from pathlib import Path

root = Path(__file__).parents[1]

gbbe = read_datapackage(root / "datapackage.json", "global-biomass-burning-emissions")

gfed4s = read_datapackage(root / "datapackage.json", "gfed4s")

df = pd.concat([gbbe.loc[:1996], gfed4s[gbbe.columns]])

df.to_csv(root / "data/gbbe-extended.csv", float_format="%.3f")
