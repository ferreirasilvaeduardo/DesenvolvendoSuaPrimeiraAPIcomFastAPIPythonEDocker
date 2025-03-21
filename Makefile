run:
	@uvicorn src.main:app --reload

precommit-install:
	@poetry run pre-commit install

test:
	@poetry run pytest

test-matching:
	@poetry run pytest -s -rx -k $(K) --pdb ./tests/

format:
	isort .
	black .
	autopep8 --in-place --recursive .

lint:
	flake8 .
	pylint $(find . -name "*.py")

type-check:
	mypy --explicit-package-bases .
	bandit -r .
