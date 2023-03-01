lock:
	poetry lock
.PHONY: lock

lint:
	autoflake --check --in-place --recursive --remove-all-unused-imports .
	isort --check --atomic .
	black --check .
	mypy .
.PHONY: lint

fmt:
	autoflake --in-place --recursive --remove-all-unused-imports .
	isort --atomic .
	black .
	mypy .
.PHONY: fmt
