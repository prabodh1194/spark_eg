PYTHON := $(shell which python3.11)
VENV = venv3.11
PIP = $(VENV)/bin/pip3.11

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  create_virtualenv   to create a virtual environment"
	@echo "  install_deps        to install dependencies"

all: help

create_virtualenv:
	virtualenv --python=$(PYTHON) $(VENV)

install_deps:
	. $(VENV)/bin/activate
	$(PIP) install poetry
	poetry install --no-interaction --no-root --with dev
