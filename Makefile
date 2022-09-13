install: # do-poetry-install
	poetry install

brain-games: # run-brain-games
	poetry run brain-games

build: # do-poetry-build:
	poetry build

publish: # publish-changes-no-pypi
	poetry publish --dry-run

package-install: # install-package
	python3 -m pip install --user dist/*.whl

lint: # use-linter
	poetry run flake8 brain_games

