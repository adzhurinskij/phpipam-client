# HELP
.PHONY: help

help: ## This help
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

# CLEAN

clean: clean-build clean-pyc clean-pycache ## Clean repository

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

clean-pycache:
	find . -name '__pycache__' -exec rm -rf {} +


# TOOLS

build: clean ## Build PyPI packet
	poetry run poetry-setup
	poetry build


# VERSIONS

bump-patch: ## Bump patch version
	poetry run poetry-setup # update setup.py and requirements.txt
	bumpversion patch

bump-minor: ## Bump minor version
	poetry run poetry-setup # update setup.py and requirements.txt
	bumpversion minor

bump-major: ## Bump major version
	poetry run poetry-setup # update setup.py and requirements.txt
	bumpversion major
