.DEFAULT_GOAL := generate

init:
	pip install requests

generate:
	@echo "Building dist wheel"
	python setup.py build_ext
