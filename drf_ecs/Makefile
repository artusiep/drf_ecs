PYTHON_CLI?=../venv/bin/python

.EXPORT_ALL_VARIABLES:

PHONY += run test make-migrations migrate load-data
.PHONY: $(PHONY)

# Local Development

run: load-data
	${PYTHON_CLI} manage.py runserver 0.0.0.0:8080 --settings=core.settings.local

test:
	${PYTHON_CLI} manage.py test --settings=core.settings.codebuild

make-migrations:
	${PYTHON_CLI} manage.py makemigrations --settings=core.settings.local

migrate: make-migrations
	${PYTHON_CLI} manage.py  migrate --settings=core.settings.local

load-data: migrate
	${PYTHON_CLI} manage.py loaddata --settings=core.settings.local user

# Dev Environment

make-migrations-dev:
	${PYTHON_CLI} manage.py makemigrations --settings=core.settings.dev

migrate-dev: make-migrations-dev
	${PYTHON_CLI} manage.py  migrate --settings=core.settings.dev

load-data-dev: migrate-dev
	${PYTHON_CLI} manage.py loaddata --settings=core.settings.dev

# QA Environment

make-migrations-qa:
	${PYTHON_CLI} manage.py makemigrations --settings=core.settings.qa

migrate-qa: make-migrations-qa
	${PYTHON_CLI} manage.py  migrate --settings=core.settings.qa

load-data-qa: migrate-qa
	${PYTHON_CLI} manage.py loaddata --settings=core.settings.qa

# Prod Environment

make-migrations-prod:
	${PYTHON_CLI} manage.py makemigrations --settings=core.settings.prod

migrate-prod: make-migrations-prod
	${PYTHON_CLI} manage.py  migrate --settings=core.settings.prod

load-data-prod: migrate-prod
	${PYTHON_CLI} manage.py loaddata --settings=core.settings.prod
