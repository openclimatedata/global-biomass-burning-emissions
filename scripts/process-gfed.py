import pandas as pd

from pandas_datapackage_reader import read_datapackage
from pathlib import Path
from pandas.util.testing import assert_almost_equal

root = Path(__file__).parents[1]

with open(root / "gfedfiles.txt", "r") as f:
    files = [Path(i).name for i in f.read().splitlines()]

out = {}

for name in files:
    path = root / "raw_data" / name
    with open(path) as f:
        # Read the 4th row with unit information
        for _ in range(3):
            f.readline()
        unit = f.readline()
        factor = int(
            unit.split("estimates in ")[1].split(" g ")[0].split("E")[1]
        )
        f.seek(0)
        data = pd.read_table(f, skiprows=8, delim_whitespace=True, nrows=15)
        data = data.set_index("Region").T.loc['1997':'2017']
        data.index = [int(i) for i in data.index]
        data = data.Global
        data = data / 10**(12 - factor)  # to Tg
        # Parse gas name from e.g. 'GFED4.1s_SO2.txt',
        # or 'GFED4.1s_Toluene_lump.txt'
        idx = path.suffixes[0].split("_", 1)[1]
        data.name = idx
        out[idx] = data

# From http://www.globalfiredata.org/ar6historic.html with NH3 removed
# as it is already contained in the data separately.
nmvoc = ["C2H6", "CH3OH", "C2H5OH", "C3H8", "C2H2", "C2H4", "C3H6", "C5H8", "C10H16", "C7H8", "C6H6", "C8H10", "Toluene_lump", "Higher_Alkenes", "Higher_Alkanes", "CH2O", "C2H4O", "C3H6O", "C2H6S", "HCN", "HCOOH", "CH3COOH", "MEK", "CH3COCHO", "HOCH2CHO"
]

df = pd.DataFrame(out)
df.index.name = "Year"
df["NMVOC"] = df[nmvoc].sum(axis=1)
df.index = pd.PeriodIndex(df.index, freq="A")
gbbe = read_datapackage(root / "datapackage.json", "global-biomass-burning-emissions")

# Test for sufficient equality of NMVOC sum with GBBE data
# where it is already combined.
assert_almost_equal(
    gbbe.NMVOC.loc['1997':'2015'].round(0),
    df["NMVOC"].loc['1997':'2015'].round(0)
)

df.to_csv(root / "data/gfed4s.csv")
