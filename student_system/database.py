# database.py
import sqlite3

# Database setup
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

def initialize_database():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            name TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id TEXT PRIMARY KEY,
            title TEXT,
            author TEXT,
            isbn TEXT
        )
    """)
    conn.commit()

def fetch_books():
    cursor.execute("SELECT * FROM books")
    return cursor.fetchall()

def close_connection():
    conn.close()