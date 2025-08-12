from redis import Redis

from src.main.infra.config.environment_settings import get_environment_variables


class RedisConfig:
    @staticmethod
    def get_redis_client() -> Redis:
        env = get_environment_variables()
        return Redis.from_url(url=env.REDIS_URL, decode_responses=True, socket_connect_timeout=5, socket_timeout=5)

    # decode_responses: decodes all the data retrieved from redis from byte string to general string. By default, False
    # socket_connect_timeout: timeout for connections
    # socket_timeout: timeout for commands.

    # After you issue a command or a connection attempt, the client will wait for a response from the server.
    # If the server doesn't respond within a certain time limit, the client will throw a TimeoutError.
    # By default, the timeout happens after 10 seconds for both connections and commands,
    # but you can set your own timeouts using the socket_connect_timeout and socket_timeout parameters when you connect
