TARGETS := hello dev-requirements requirements lint black lab process view clean all
TAG := $(shell git rev-parse --short HEAD)

hello:
	@echo make [$(TARGETS)]

dev-requirements: requirements
	pip install --quiet --upgrade --requirement dev-requirements.txt

requirements:
	pip install --upgrade pip
	pip install --upgrade --requirement requirements.txt

lint:
	flake8 --ignore=E501,W503 *.py
	black --diff *.py

black:
	black *.py
	black --ipynb *.ipynb

analysis:
	python3 ./cluster_analysis.py

clean:
	-rm -vf ./data/*.json
	-rm -rvf __pycache__/

all: requirements analysis

.PHONY: $(TARGETS)
