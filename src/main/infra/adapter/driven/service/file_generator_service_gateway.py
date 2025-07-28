from typing import List

from src.main.application.port.driven.file.file_generator_service import FileGeneratorService
from src.main.domain.history import History
from src.main.infra.adapter.driven.service.csv_generator import CSVGenerator


class FileGeneratorServiceGateway(FileGeneratorService):
    def __init__(self, csv_generator: CSVGenerator):
        self._csv_generator = csv_generator

    def generate_history_file(self, histories: List[History]) -> bytes:
        headers = FileGeneratorServiceGateway._generate_history_headers(histories)
        rows = FileGeneratorServiceGateway._generate_history_rows(histories)
        return self._csv_generator.generate_csv(headers, rows, delimiter=',')

    @staticmethod
    def _generate_history_headers(histories: List[History]) -> List[str]:
        if not histories:
            return []
        dates = set()
        for history in histories:
            dates.update(history.rating_history.keys())
        sorted_dates = sorted(dates)
        headers = ['username'] + sorted_dates
        return headers

    @staticmethod
    def _generate_history_rows(histories: List[History]) -> List[str]:
        rows = []
        for history in histories:
            row = [history.player_username]
            sorted_dates = sorted(history.rating_history.keys())
            for date in sorted_dates:
                row.append(str(history.rating_history[date]))
            rows.append(row)
        return rows
