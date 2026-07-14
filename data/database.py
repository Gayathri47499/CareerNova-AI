import sqlite3
from pathlib import Path

# Create data directory if it doesn't exist
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

DATABASE_PATH = DATA_DIR / "career_history.db"


def get_connection():

    connection = sqlite3.connect(
        DATABASE_PATH,
        check_same_thread=False
    )

    connection.row_factory = sqlite3.Row

    return connection