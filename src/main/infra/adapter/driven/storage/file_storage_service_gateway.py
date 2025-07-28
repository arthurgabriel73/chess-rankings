from src.main.application.port.driven.file.file_storage_service import FileStorageService
from src.main.infra.adapter.driven.storage.storage_service import StorageService


class FileStorageServiceGateway(FileStorageService):
    def __init__(self, storage_service: StorageService):
        self._storage_service = storage_service

    def upload_file(self, key: str, file: bytes) -> None:
        return self._storage_service.upload(key, file)

    def get_file_url(self, key: str) -> str:
        return self._storage_service.get_url(key)

    def get_file_download_url(self, key: str) -> str:
        return self._storage_service.get_download_url(key)
