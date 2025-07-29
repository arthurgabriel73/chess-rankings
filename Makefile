include .env.test
include .env.local

.PHONY: build up down clean remove-image logs

export PYTHONPATH=$(pwd)
export ENV=test

test:
	@echo "\033[0;36mRunning all tests...\033[0m"
	poetry run coverage run -m pytest -v src/test/unit
	poetry run coverage run -m pytest -v src/test/integration
	poetry run coverage combine
	poetry run coverage report --fail-under=80
	poetry run coverage html
	@echo "\033[0;32mAll tests completed successfully!\033[0m"

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

e2e: setup-localstack setup-redis setup-mock-chess-api
	@echo "\033[0;36mRunning e2e tests...\033[0m"
	poetry run coverage run --source=./ -m behave || (echo "\033[0;31mTests failed!\033[0m" && docker-compose down && exit 1)
	poetry run coverage report --fail-under=80
	poetry run coverage html
	@echo "\033[0;32me2e tests completed successfully!\033[0m"
	make teardown-mock-chess-api
	docker-compose down

setup-mock-chess-api:
	@echo "\033[0;36mSetting up mock server...\033[0m"
	docker build -f src/test/resources/mock_api.Dockerfile -t mock_chess_api_service .
	docker run -d --name mock-chess-api -p 9000:9000 mock_chess_api_service

teardown-mock-chess-api:
	@echo "\033[0;36mTearing down mock server...\033[0m"
	docker stop mock-chess-api || true
	docker rm mock-chess-api || true

e2e-cleanup:
	@echo "\033[0;36mCleaning up containers...\033[0m"
	docker-compose down

setup-localstack:
	@echo "\033[0;36mInitializing LocalStack...\033[0m"
	export AWS_ACCESS_KEY_ID=local-access-key-id
	export AWS_USER_ACCESS_KEY_VALUE=local-secret-access-key
	export AWS_DEFAULT_REGION=us-east-1
	docker-compose up -d localstack
	sleep 5
	curl -s -X PUT http://localhost:4566/chess-rankings-local
	@echo "\033[0;32mLocalStack initialized with S3 bucket!\033[0m"

setup-redis:
	@echo "\033[0;36mSetting up Redis...\033[0m"
	docker-compose up -d redis
	@echo "\033[0;32mRedis setup completed!\033[0m"

setup-app:
	@echo "\033[0;36mStarting the application...\033[0m"
	docker-compose up app --build
	@echo "\033[0;32mApplication started successfully!\033[0m"


up: setup-localstack setup-redis setup-app

down:
	@echo "\033[0;36mStopping all services...\033[0m"
	docker-compose down
	@echo "\033[0;32mAll services stopped successfully!\033[0m"