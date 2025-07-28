from abc import ABC, abstractmethod


class StorageService(ABC):
    @abstractmethod
    def upload(self, key: str, file: bytes) -> None:
        pass

    @abstractmethod
    def get_url(self, key: str) -> str:
        pass

    @abstractmethod
    def get_download_url(self, key: str) -> str:
        pass
