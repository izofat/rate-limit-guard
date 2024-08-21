SHELL := /bin/bash
PROJECT_NAME := LX-Scanner-API
CURDIR := $(shell pwd)
PATH_IMAGE ?= $(CURDIR)/tests/data/testocr.png
LANGUAGE_IMAGE ?= en

POETRY := ~/.local/bin/poetry

install:
	@poetry install
	@poetry run mypy --install-types

format:
	@poetry run autoflake --in-place --remove-all-unused-imports --recursive --remove-unused-variables \
		--ignore-init-module-imports .
	@poetry run isort .
	@poetry run black .

type-check:
	@poetry run mypy rate_limit_guard
	@poetry run mypy tests

lint:
	@poetry run pylint rate_limit_guard
	@poetry run pylint tests
	@poetry run bandit -r rate_limit_guard

config:
	@cp docs/config.example.toml ./config.toml

test:
	@poetry run pytest
