include .env.test

.PHONY: build up down clean remove-image logs

export ENV=test
export PYTHONPATH=$(pwd)

test: unit integration

unit:
	@echo "\033[0;36mRunning unit tests...\033[0m"
	poetry run coverage run -m pytest -v src/test/unit
	poetry run coverage report --fail-under=80
	poetry run coverage html
	@echo "\033[0;32mUnit tests completed successfully!\033[0m"

integration:
	@echo "\033[0;36mRunning integration tests...\033[0m"
	poetry run coverage run -m pytest -v src/test/integration
	poetry run coverage report --fail-under=80
	poetry run coverage html
	@echo "\033[0;32mIntegration tests completed successfully!\033[0m"