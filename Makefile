.PHONY init
init:
	poetry lock --no-update
	poetry install --no-interaction --no-root --no-ansi

.PHONY run
run:
	python -m app.detect_human