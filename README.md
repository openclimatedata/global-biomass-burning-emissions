# Global Biomass Burning Emissions

CMIP6 Forcing Datasets Summary: http://goo.gl/r8up31

## Preparation

Files to download are selected from https://esgf-data.dkrz.de/search/esgf-dkrz/,
selecting VUA as "Institution ID" and the following variables:

- BC (1)
- CH4 (1)
- CO (1)
- N2O (1)
- NH3 (1)
- NMVOC (1)
- NOx (1)
- OC (1)
- SO2 (1)
- gridcellarea (1)

The result list with direct HTTP links and checksums is stored in `files.txt`.

To download the files into `raw_data` run `make download`. This requires around
11 GB of disk space.

Downloaded files are processed in `scripts/process.py` and saved as annual
values in `data/global-biomass-burning-emissions.csv`.

Run `make` to generate the CSV file from the downloaded files.


## License

This Data Package is based on data from

VUA 1.2 Global Biomass Burning Emissions prepared for input4MIPs

Vrije Universiteit Amsterdam, De Boelelaan 1105, 1081 HV Amsterdam, Netherlands

Biomass burning emissions data produced by VUA is licensed under a Creative Commons Attribution "Share Alike" 4.0 International License (http://creativecommons.org/licenses/by/4.0/). The data producers and data providers make no warranty, either express or implied, including but not limited to, warranties of merchantability and fitness for a particular purpose. All liabilities arising from the supply of the information (including any liability arising in negligence) are excluded to the fullest extent permitted by law.

GFED4s data notes for Citation:

Please mention you used fire emissions from the Global Fire Emissions Database
version 4 (GFED4s) described in van der Werf et al. (2017). When fires are a key
focus  of  your  paper  please  also  include  a  citation  to  the  original
burned  area paper (Giglio et al., 2013) boosted by small fire burned area following
Randerson et  al.  (2012)
.
