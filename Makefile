all: process-gfed

venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur scripts/requirements.txt
	touch venv

process: files.txt venv
	./venv/bin/python scripts/process.py

process-gfed: scripts/process-gfed.py venv
	./venv/bin/python scripts/process-gfed.py

download:
	./scripts/download.sh

download-gfed:
	./scripts/download_gfed.sh

clean:
	rm -rf data/*.csv venv

.PHONY: clean download
