# Global Biomass Burning Emissions

Files to download are selected from https://esgf-data.dkrz.de/search/esgf-dkrz/,
selecting VUA as "Institution ID" and the following variables:

BC (1)
CH4 (1)
CO (1)
N2O (1)
NH3 (1)
NMVOC (1)
NOx (1)
OC (1)
SO2 (1)
gridcellarea (1)

The result list with opened HTTP links and checksums is pasted in `files.txt`.

Do download the files into `raw_data` run `make data`.

Downloaded files are processed in `scripts/process.py` and saved as annual
values in `data/global-fire-emissions.csv`.

Run `make process` to generate the CSV file.

# License

This Data Package is based on data from

VUA 1.2 Global Biomass Burning Emissions prepared for input4MIPs

Vrije Universiteit Amsterdam, De Boelelaan 1105, 1081 HV Amsterdam, Netherlands

Biomass burning emissions data produced by VUA is licensed under a Creative Commons Attribution "Share Alike" 4.0 International License (http://creativecommons.org/licenses/by/4.0/). The data producers and data providers make no warranty, either express or implied, including but not limited to, warranties of merchantability and fitness for a particular purpose. All liabilities arising from the supply of the information (including any liability arising in negligence) are excluded to the fullest extent permitted by law.
