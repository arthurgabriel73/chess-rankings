from abc import ABC, abstractmethod
from typing import List

from src.main.domain.history import History


class FileGeneratorService(ABC):
    @abstractmethod
    def generate_history_file(self, histories: List[History]) -> bytes:
        pass
