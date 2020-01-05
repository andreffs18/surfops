.PHONY: pull build run shell
SHELL := /bin/bash

build:
	docker build -t andreffs/surfops:latest -f Dockerfile .

push:
	docker push andreffs/surfops:latest

pull:
	docker pull andreffs/surfops

shell:
	docker run -it --rm --name surfops -v $(shell pwd):/surfops --env-file .env andreffs/surfops /bin/sh

run: shell
	pipenv install && pipenv shell
