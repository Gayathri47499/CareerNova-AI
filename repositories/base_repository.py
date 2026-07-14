import json
from pathlib import Path
from typing import Any


class BaseRepository:

    def __init__(self, file_path: Path):
        self.file_path = file_path

    def load_json(self) -> Any:

        try:

            with open(self.file_path, "r", encoding="utf-8") as file:

                return json.load(file)

        except FileNotFoundError:

            raise FileNotFoundError(
                f"Knowledge file not found: {self.file_path}"
            )