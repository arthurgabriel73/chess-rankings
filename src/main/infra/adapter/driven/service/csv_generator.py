import csv
from io import StringIO
from typing import List


class CSVGenerator:
    @staticmethod
    def generate_csv(headers: List, rows: List, delimiter: str) -> bytes:
        CSVGenerator._validate_delimiter(delimiter)
        output = StringIO()
        writer = csv.writer(output, delimiter=delimiter)
        writer.writerow(headers)
        writer.writerows(rows)
        file = output.getvalue().encode('utf-8')
        output.close()
        return file

    @staticmethod
    def _validate_delimiter(delimiter: str) -> None:
        if delimiter not in [',', ';', '|']:
            raise ValueError(f"Invalid delimiter: {delimiter}. Supported delimiters are: ',', ';', '|'")
