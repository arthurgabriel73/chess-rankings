include .env.test
include .env.local

.PHONY: build up down clean remove-image logs

export ENV=test
export PYTHONPATH=$(pwd)

test:
	poetry run coverage run -m pytest -v src/test/unit
	poetry run coverage run -m pytest -v src/test/integration
	poetry run coverage combine
	poetry run coverage report --fail-under=80
	poetry run coverage html

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

setup-localstack:
	@echo "\033[0;36mInitializing LocalStack...\033[0m"
	export AWS_ACCESS_KEY_ID=local-access-key-id
	export AWS_USER_ACCESS_KEY_VALUE=local-secret-access-key
	export AWS_DEFAULT_REGION=us-east-1
	docker-compose up -d localstack
	sleep 5
	curl -s -X PUT http://localhost:4566/chess-rankings-local
	@echo "\033[0;32mLocalStack initialized with S3 bucket!\033[0m"