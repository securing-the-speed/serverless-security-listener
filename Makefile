ROOT_DIR	:= $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PARENTDIR   := $(realpath ../)
AWS_REGION	:= us-west-2
GITHASH 	:= $(shell git rev-parse --short HEAD)

.PHONY:all
all:
	@echo 'Available make targets:'
	@grep '^[^#[:space:]\.PHONY.*].*:' Makefile

.PHONE: setup 
setup:
	@echo "Some stuff goes here"

.PHONY: test
test:
	python3 -m pytest 

.PHONY: clean
clean:
	rm -rf .pytest_cache
	rm -rf serverless_security_scanner/__pycache__