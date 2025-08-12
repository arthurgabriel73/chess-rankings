from src.main.infra.config.environment_settings import get_env_filename, get_environment_variables


class TestGetEnvironmentVariables:
    def test_get_environment_variables(self):
        get_env_filename.cache_clear()
        env = get_environment_variables()
        print(env.model_dump())
        assert env.APP_NAME == 'chess_rankings_test'
        assert env.APP_HOST == 'localhost'
        assert env.APP_PORT == 3000
        assert env.LICHESS_API_BASE_URL == 'http://0.0.0.0:9000'
        assert env.AWS_BUCKET_NAME == 'chess-rankings-local'
        assert env.AWS_USER_KEY_ID == 'my-test-aws-user-key-id'
        assert env.AWS_USER_ACCESS_KEY == 'my-test-aws-user-access-key'
        assert env.AWS_REGION == 'us-west-2'
        assert env.AWS_ENDPOINT_URL == 'http://localhost:4566'
        assert env.REDIS_URL == 'redis://localhost:6379/0'
