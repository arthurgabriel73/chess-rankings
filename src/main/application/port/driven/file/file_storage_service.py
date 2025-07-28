from abc import ABC, abstractmethod


class FileStorageService(ABC):
    @abstractmethod
    def upload_file(self, key: str, file: bytes) -> None:
        pass

    @abstractmethod
    def get_file_url(self, key: str) -> str:
        pass

    @abstractmethod
    def get_file_download_url(self, key: str) -> str:
        pass
