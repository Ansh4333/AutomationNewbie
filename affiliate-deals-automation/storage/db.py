import sqlite3

def get_db():
    conn = sqlite3.connect("deals.db")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS deals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT UNIQUE,
        source TEXT
    )
    """)
    return conn
