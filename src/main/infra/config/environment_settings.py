import os
from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


@lru_cache
def get_env_filename():
    runtime_env = os.getenv('ENV')
    return f'.env.{runtime_env}' if runtime_env else '.env'


class EnvironmentSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=get_env_filename(), env_ignore_empty=True, populate_by_name=True, extra='allow', env_prefix='AAA_'
    )
    # The environment variable name is overridden using validation_alias. In this case, the environment variable APP_NAME_VALUE will be read instead of APP_NAME.
    # But if APP_NAME_VALUE is not present, it will get from APP_NAME, only is there is no APP_NAME_VALUE
    # APP_NAME: str = Field(validation_alias='APP_NAME_VALUE', default='chess_rankings')
    APP_NAME: str = Field(validation_alias='APP_NAME_VALUE', default='chess_rankings')
    APP_HOST: str = Field(validation_alias='APP_HOST_VALUE', default='localhost')
    APP_PORT: int = Field(validation_alias='APP_PORT_VALUE', default='3000')
    LICHESS_API_BASE_URL: str = Field(validation_alias='LICHESS_API_BASE_URL_VALUE', default='http://0.0.0.0:9000')
    AWS_BUCKET_NAME: str = Field(validation_alias='AWS_BUCKET_NAME_VALUE', default='my-chess-bucket')
    AWS_USER_KEY_ID: str = Field(validation_alias='AWS_USER_KEY_ID_VALUE', default='my-aws-user-key-id')
    AWS_USER_ACCESS_KEY: str = Field(validation_alias='AWS_USER_ACCESS_KEY_VALUE', default='my-aws-user-access-key')
    AWS_REGION: str = Field(validation_alias='AWS_REGION_VALUE', default='us-west-2')
    AWS_ENDPOINT_URL: str = Field(validation_alias='AWS_ENDPOINT_URL_VALUE', default='http://localhost:4566')
    REDIS_URL: str = Field(validation_alias='REDIS_URL_VALUE', default='redis://localhost:6379/0')


@lru_cache
def get_environment_variables():
    return EnvironmentSettings()
