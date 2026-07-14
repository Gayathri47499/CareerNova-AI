from data.database import get_connection


def initialize_database():

    connection = get_connection()
    cursor = connection.cursor()

    # -----------------------------
    # Users Table
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        full_name TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    # -----------------------------
    # Career Events
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS career_events(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        event_type TEXT,

        event_data TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    # -----------------------------
    # Resume Table
    # -----------------------------
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        name TEXT,

        email TEXT,

        phone TEXT,

        resume_json TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    connection.commit()
    connection.close()


if __name__ == "__main__":

    initialize_database()

    print("Database Initialized Successfully")