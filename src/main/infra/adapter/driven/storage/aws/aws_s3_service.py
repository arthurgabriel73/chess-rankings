from src.main.infra.adapter.driven.storage.storage_service import StorageService


class AwsS3Service(StorageService):
    def upload(self, key: str, file: bytes) -> None:
        pass

    def get_url(self, key: str) -> str:
        pass

    def get_download_url(self, key: str) -> str:
        pass
