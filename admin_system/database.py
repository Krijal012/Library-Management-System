# database.py
import sqlite3
import tkinter as tk  # Import tkinter here

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
    conn.commit()

def refresh_table(tree):
    for i in tree.get_children():
        tree.delete(i)
    
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    
    for student in students:
        tree.insert("", tk.END, values=student)  # Now tk.END is available