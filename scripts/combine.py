import pandas as pd

from pandas_datapackage_reader import read_datapackage
from pathlib import Path

root = Path(__file__).parents[1]

dp = read_datapackage(root / "datapackage.json")

df = pd.concat([
    dp["global-biomass-burning-emissions"].loc[:1996],
    dp["gfed4s"][dp["global-biomass-burning-emissions"].columns]
    ])

df.to_csv(root / "data/gbbe-extended.csv", float_format="%.3f")
