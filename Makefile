.DEFAULT_GOAL := help
.PHONY: tox tox-current test lint submodule generate release format help

REPO_ROOT:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

BUF_VERSION="1.36.0"
BIN="venv/bin"

venv: ## install deps (library & development)
	python3 -m venv venv
	$(BIN)/python3 -m pip install --upgrade pip
	$(BIN)/python3 -m pip install -r requirements-dev.txt
	@ curl --fail --silent --show-error --location \
		"https://github.com/bufbuild/buf/releases/download/v${BUF_VERSION}/buf-$(shell uname -s)-$(shell uname -m)" \
		-o "$(BIN)/buf" && \
		chmod +x "$(BIN)/buf"

tox: ## run ALL checks for ALL available python versions
	$(BIN)/python3 -m tox

tox-current: ## run ALL checks ONLY for current python version
	python3 -m tox -e `python3 -c 'import platform; print("py" + "".join(platform.python_version_tuple()[:2]))'`

test: ## run tests ONLY for current python version
	$(BIN)/python3 -m pytest

lint: ## run linters, formatters for current python versions
	$(BIN)/python3 -m flake8 doublecloud examples tests setup.py changelog.py
	$(BIN)/python3 -m pylint doublecloud examples tests setup.py changelog.py
	$(BIN)/python3 -m isort --check-only doublecloud setup.py changelog.py
	$(BIN)/python3 -m black --check doublecloud setup.py changelog.py

format:
	$(BIN)/python3 -m isort doublecloud setup.py changelog.py examples
	$(BIN)/python3 -m black doublecloud setup.py changelog.py examples

submodule:  ## retrieve public protospecs
	git submodule update --init --recursive --remote

clean: ## clean environment and generated code
	@ rm -rf doublecloud/{clickhouse,kafka,network,transfer,v1,visualization} 
	@ rm -rf venv

generate: submodule venv ## generate code from specifications
	cp buf.yaml api/buf.yaml
	cp buf.gen.yaml api/buf.gen.yaml
	cd api; ../venv/bin/buf dep update
	cd api; ../venv/bin/buf generate

	find doublecloud -type d -exec touch {}/__init__.py \;

release:  ## update changelog, bump version, build and publish package to pypi
	venv/bin/python -m semantic_release publish --minor

help: ## Show help message
	@IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##/:/'`); \
	printf "%s\n\n" "Usage: make [task]"; \
	printf "%-20s %s\n" "task" "help" ; \
	printf "%-20s %s\n" "------" "----" ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$':' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf '\033[36m'; \
		printf "%-20s %s" $$help_command ; \
		printf '\033[0m'; \
		printf "%s\n" $$help_info; \
	done
