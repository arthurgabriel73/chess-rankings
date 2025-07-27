from src.main.infra.config.environment_settings import get_env_filename, get_environment_variables


class TestGetEnvironmentVariables:
    def test_get_environment_variables(self):
        get_env_filename.cache_clear()
        env = get_environment_variables()
        assert env.APP_NAME == 'chess_rankings_test'
        assert env.APP_HOST == 'localhost'
        assert env.APP_PORT == 3000
        assert env.LICHESS_API_BASE_URL == 'https://lichess.org/api'
