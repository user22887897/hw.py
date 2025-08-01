

import sqlite3

def get_connection():
    return sqlite3.connect("fleet.db")

def create_table():
    conn = get_connection()
    cur = conn.cursor()


    cur.execute("""
        CREATE TABLE IF NOT EXISTS vehicles(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL,
                brand TEXT NOT NULL,
                model TEXT NOT NULL,
                year INTEGER NOT NULL,
                searts INTEGER,
                has_sidecar BOOLEAN
            )
    """)
    conn.commit()
    conn.close()