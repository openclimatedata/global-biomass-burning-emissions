import pandas as pd

from pathlib import Path

root = Path(__file__).parents[1]

with open(root / "gfedfiles.txt", "r") as f:
    files = [Path(i).name for i in f.read().splitlines()]

out = {}

for name in files:
    path = root / "raw_data" / name
    with open(path) as f:
        data = pd.read_table(f, skiprows=8, delim_whitespace=True, nrows=15)
        data = data.set_index("Region").T.loc['1997':'2018']
        data.index = [int(i) for i in data.index]
        data = data.Global
        # Parse gas name from e.g. 'GFED4.1s_SO2.txt'
        idx = path.suffixes[0].split("_")[1]
        data.name = idx
        out[idx] = data

df = pd.DataFrame(out)
df.index.name = "Year"
df.to_csv(root / "data/gfed4s.csv")
