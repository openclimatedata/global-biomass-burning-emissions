import xarray as xr
import pandas as pd
import numpy as np

from calendar import monthrange
from pathlib import Path
from hashlib import sha256
from math import isclose
from tqdm import tqdm


root = Path(__file__).parents[1]

with open(root / "files.txt", "r") as f:
    lines = f.read().splitlines()
    files = [l.split(" ") for l in lines]

gridcellarea = xr.open_dataset(
    root
    / "raw_data/gridcellarea-em-biomassburning_input4MIPs_emissions_CMIP_VUA-CMIP-BB4CMIP6-1-2_gn.nc"
).gridcellarea


def calculate_annual_series(nc_filepath):
    """Return aggregated, annual series"""
    ds = xr.open_dataset(nc_filepath)
    name = ds.variable_id
    assert ds[name].units == "kg m-2 s-1"
    series = pd.Series()
    series.name = name
    years = np.unique(ds.time.dt.year)
    for year in tqdm(years):
        sel = ds[name].sel(time=str(year))
        days_in_year = [
            v[1]
            for v in [
                monthrange(int(i.dt.year.values), int(i.dt.month.values))
                for i in sel.time
            ]
        ]
        sel_kg_s = sel * gridcellarea
        sel_monthly_kg = (
            sel_kg_s.sum(dim=["latitude", "longitude"]).to_series()
            * days_in_year
            * 24
            * 3600
        )
        sel_annual_Tg = sel_monthly_kg.sum() / 10 ** 9
        series.at[year] = sel_annual_Tg

    print(
        "\t Check first value: ",
        np.round(series.iloc[0], 2),
        float(ds.annual_total_first_year_Tg_yr),
    )
    assert np.round(series.iloc[0], 2) == float(ds.annual_total_first_year_Tg_yr)

    print(
        "\t Check last value: ",
        np.round(series.iloc[-1], 2),
        float(ds.annual_total_last_year_Tg_yr),
    )
    assert np.round(series.iloc[-1], 2) == float(ds.annual_total_last_year_Tg_yr)
    return series


df = pd.DataFrame(index=range(1750, 2016))
df.index.name = "Year"

for url, checksum in files:
    name = Path(url).name
    filepath = root / "raw_data" / name
    if filepath.exists():
        print("Processing {}".format(name))
        with open(filepath, "rb") as f:
            content = f.read()
            assert sha256(content).hexdigest() == checksum
            print("\tChecksum ok.")
        if "gridcell" in name:
            continue
        annual_series = calculate_annual_series(filepath)
        if annual_series.name in df.columns:
            df[annual_series.name].update(annual_series)
        else:
            df = df.join(annual_series)
    else:
        print("Not found: {}.".format(name))

print(df.head())
print(df.tail())

df.to_csv(root / "data/global-biomass-burning-emissions.csv")
