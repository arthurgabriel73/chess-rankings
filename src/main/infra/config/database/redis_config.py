import redis


class RedisConfig:
    @staticmethod
    def get_redis_client() -> redis.Redis:
        return redis.Redis.from_url(
            url='redis://localhost:6379/0', decode_responses=True, socket_connect_timeout=5, socket_timeout=5
        )
