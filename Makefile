.PHONY: all

SHELL=/bin/bash -e

.DEFAULT_GOAL := help

DC=docker-compose
STORES=docker-compose/storages.yml
MONITORING=docker-compose/monitoring.yml
APP=docker-compose/app.yml

# app
lint:
	poetry run python -m flake8 ./

format:
	poetry run autopep8 --aggressive --experimental -r -i ./ 
	poetry run python -m isort ./
	poetry run black --fast ./

migrate:
	poetry run python -m alembic upgrade head

makemigration:
	poetry run python -m alembic revision --autogenerate

# docker-compoe
up-storages:
	${DC} -f ${STORES} up -d

up-monitoring:
	${DC} -f ${MONITORING} up -d

up-all:
	${DC} -f ${STORES} -f ${MONITORING} -f ${APP} up -d

stop-all:
	${DC} -f ${STORES} -f ${MONITORING} stop