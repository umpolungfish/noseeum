# Makefile for noseeum

.PHONY: install uninstall clean

install:
	pip install -r requirements.txt
	pip install .

uninstall:
	pip uninstall -y noseeum

clean:
	rm -rf build dist noseeum.egg-info
