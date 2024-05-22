# Variables
ENV_FILE = .env
DOCKER_COMPOSE = docker-compose
PYTHON = python3
PIP = pip3
APP = app.py

# Targets
.PHONY: help install build up down clean test

help:
	@echo "Usage:"
	@echo "  make install          Install Python dependencies"
	@echo "  make build            Build Docker images"
	@echo "  make test             Run tests"
	@echo "  make generate-api     Generate API from OpenAPI spec"
	@echo "  make test             Run tests"

install:
	$(PIP) install -r requirements.txt

build:
	$(DOCKER_COMPOSE) up --build -d

test:
	$(PYTHON) -m unittest discover -s tests

run:
	uvicorn questionnaire.main:app --reload

generate-api:
	docker run --rm -u $(id -u ${USER}):$(id -g ${USER}) -v ${PWD}/contract:/local openapitools/openapi-generator-cli:v7.5.0 generate -i /local/openapi.spec.yaml -g python-fastapi -o /local/oas-generator-out/python

generate-models:
	docker run --rm -u $(id -u ${USER}):$(id -g ${USER}) -v ${PWD}/contract:/local openapitools/openapi-generator-cli:v7.5.0 generate -i /local/openapi.spec.yaml -g python-fastapi -o /local/oas-generator-out/python && rm -rf ./src/openapi_server/models && mkdir ./src/openapi_server/models && mv contract/oas-generator-out/python/src/openapi_server/models ./src/openapi_server/models && rm -rf contract/oas-generator-out
