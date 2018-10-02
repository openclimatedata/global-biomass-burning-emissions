all: data/gbbe-extended.csv

venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur scripts/requirements.txt
	touch venv

data/gbbe-extended.csv: scripts/combine.py data/global-biomass-burning-emissions.csv data/gfed4s.csv
	./venv/bin/python $<

data/global-biomass-burning-emissions.csv: scripts/process.py files.txt venv
	./venv/bin/python $<

data/gfed4s.csv: scripts/process-gfed.py venv
	./venv/bin/python $<

download-gbbe:
	./scripts/download.sh

download-gfed:
	./scripts/download_gfed.sh

clean:
	rm -rf data/*.csv venv

.PHONY: clean download
