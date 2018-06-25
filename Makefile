all: process

venv: scripts/requirements.txt
	[ -d ./venv ] || python3 -m venv venv
	./venv/bin/pip install --upgrade pip
	./venv/bin/pip install -Ur scripts/requirements.txt
	touch venv

process: venv files.txt
	./venv/bin/python scripts/process.py

download:
	./scripts/download.sh

clean:
	rm -rf data/*.csv venv

.PHONY: clean download
