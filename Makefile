.PHONY: help init lint test

help:
	@echo AVAILABLE COMMANDS
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-23s\033[0m%s\n", $$1, $$2}'

init: ## Initialise repo for local development
	@uv sync
	@uv run pre-commit install --install-hooks

lint: ## Lint files
	uv run pre-commit run ruff

test: ## Run tests
	@uv run pytest
