import redis

from src.main.infra.config.environment_settings import get_environment_variables


class RedisConfig:
    @staticmethod
    def get_redis_client() -> redis.Redis:
        env = get_environment_variables()
        return redis.Redis.from_url(
            url=env.REDIS_URL, decode_responses=True, socket_connect_timeout=5, socket_timeout=5
        )
