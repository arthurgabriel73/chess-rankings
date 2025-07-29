from typing import Any

import boto3

from src.main.infra.adapter.driven.storage.storage_service import StorageService
from src.main.infra.config.environment_settings import get_environment_variables

env = get_environment_variables()


class AwsS3Service(StorageService):
    _s3_client: Any

    def __init__(self):
        self._s3_client = None
        self.bucket_name = env.AWS_BUCKET_NAME

    def _get_s3_client(self):
        if self._s3_client is None:
            self._s3_client = boto3.client(
                's3',
                aws_access_key_id=env.AWS_USER_KEY_ID,
                aws_secret_access_key=env.AWS_USER_ACCESS_KEY,
                region_name=env.AWS_REGION,
                endpoint_url=env.AWS_ENDPOINT_URL,
            )
        return self._s3_client

    def upload(self, key: str, file: bytes) -> None:
        s3_client = self._get_s3_client()
        s3_client.put_object(Bucket=self.bucket_name, Key=key, Body=file)

    def get_url(self, key: str) -> str:
        s3_client = self._get_s3_client()
        url = s3_client.generate_presigned_url(
            'get_object', Params={'Bucket': self.bucket_name, 'Key': key}, ExpiresIn=3600
        )
        return url

    def get_download_url(self, key: str) -> str:
        s3_client = self._get_s3_client()
        url = s3_client.generate_presigned_url(
            'get_object', Params={'Bucket': self.bucket_name, 'Key': key}, ExpiresIn=3600
        )
        return url
