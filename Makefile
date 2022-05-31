lock:
	poetry lock
.PHONY: lock

lint:
	poetry run autoflake --check -i -r --remove-all-unused-imports .
	poetry run isort --check --atomic .
	poetry run black --check .
	poetry run mypy .
.PHONY: lint

fmt:
	poetry run autoflake -i -r --remove-all-unused-imports .
	poetry run isort --atomic .
	poetry run black .
.PHONY: fmt
