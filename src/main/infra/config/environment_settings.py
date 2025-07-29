import os
from functools import lru_cache
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


@lru_cache
def get_env_filename():
    runtime_env = os.getenv('ENV')
    return f'.env.{runtime_env}' if runtime_env else '.env'


class EnvironmentSettings(BaseSettings):
    APP_NAME: Optional[str] = Field(validation_alias='APP_NAME_VALUE') or 'chess_rankings'
    APP_HOST: Optional[str] = Field(validation_alias='APP_HOST_VALUE') or 'localhost'
    APP_PORT: Optional[int] = Field(validation_alias='APP_PORT_VALUE') or '3000'
    LICHESS_API_BASE_URL: Optional[str] = Field(validation_alias='LICHESS_API_BASE_URL_VALUE') or 'http://test_lichess'
    AWS_BUCKET_NAME: Optional[str] = Field(validation_alias='AWS_BUCKET_NAME_VALUE') or 'my-chess-bucket'
    AWS_USER_KEY_ID: Optional[str] = Field(validation_alias='AWS_USER_KEY_ID_VALUE') or 'my-aws-user-key-id'
    AWS_USER_ACCESS_KEY: Optional[str] = Field(validation_alias='AWS_USER_ACCESS_KEY_VALUE') or 'my-aws-user-access-key'
    AWS_REGION: Optional[str] = Field(validation_alias='AWS_REGION_VALUE') or 'us-west-2'
    AWS_ENDPOINT_URL: Optional[str] = Field(validation_alias='AWS_ENDPOINT_URL_VALUE') or 'http://localhost:4566'
    model_config = SettingsConfigDict(
        env_file=get_env_filename(), env_ignore_empty=True, populate_by_name=True, extra='allow'
    )


@lru_cache
def get_environment_variables():
    return EnvironmentSettings()
