import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import subprocess

# Database setup
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

def initialize_database():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT,
            password TEXT,
            role TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id TEXT PRIMARY KEY,
            name TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            book_id TEXT PRIMARY KEY,
            title TEXT,
            author TEXT,
            isbn TEXT
        )
    """)
    conn.commit()

# Predefined credentials
admin_credentials = {"240319": "krijal"}
librarian_credentials = {
    "240576": "prashanna",
    "240421": "suyes",
    "240399": "reshav"
}
student_password = "student123"

# Function to handle login
def login():
    user_id = entry_id.get().strip()
    password = entry_password.get().strip()
    selected_role = role_var.get()
    
    # Check Admin credentials
    if selected_role == "Admin" and user_id in admin_credentials and admin_credentials[user_id] == password:
        subprocess.run(["python", "admindashboard.py"])
        return
    
    # Check Librarian credentials
    if selected_role == "Librarian" and user_id in librarian_credentials and librarian_credentials[user_id] == password:
        subprocess.run(["python", "librariandashboard.py"])
        return
    
    # Check Student credentials
    if selected_role == "Student" and password == student_password:
        subprocess.run(["python", "studentdashboard.py"])
        return
    
    # If none of the above, show error
    messagebox.showerror("Error", "Invalid ID or Password!")

# Function to add student
def add_student(student_id, student_name):
    try:
        cursor.execute("INSERT INTO students VALUES (?, ?)", (student_id, student_name))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

# Function to remove student
def remove_student(student_id):
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()
    if student:
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        return True
    return False

# Function to fetch students
def fetch_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

# Function to add book
def add_book(book_id, title, author, isbn):
    try:
        cursor.execute("INSERT INTO books VALUES (?, ?, ?, ?)", (book_id, title, author, isbn))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

# Function to remove book
def remove_book(book_id):
    cursor.execute("SELECT * FROM books WHERE book_id = ?", (book_id,))
    book = cursor.fetchone()
    if book:
        cursor.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
        conn.commit()
        return True
    return False

# Function to fetch books
def fetch_books():
    cursor.execute("SELECT * FROM books")
    return cursor.fetchall()

# Function to close the database connection
def close_connection():
    conn.close()

# GUI setup for login
def setup_login_gui():
    global entry_id, entry_password, role_var

    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("400x300")
    root.configure(bg="lightblue")

    frame = tk.Frame(root, bg="black", padx=10, pady=10)
    frame.pack(pady=20)

    tk.Label(root, text="Login", font=("Arial", 14, "bold"), bg="lightblue").pack()

    # Role selection
    role_var = tk.StringVar(root)
    role_var.set("Admin")  # default value
    roles = ["Admin", "Librarian", "Student"]

    tk.Label(frame, text="Role:", font=("Arial", 12), fg="white", bg="black").grid(row=0, column=0, sticky="w", pady=5)
    role_menu = tk.OptionMenu(frame, role_var, *roles)
    role_menu.config(font=("Arial", 12), width=27)
    role_menu.grid(row=0, column=1, pady=5)

    # Labels and entry fields
    tk.Label(frame, text="User ID:", font=("Arial", 12), fg="white", bg="black").grid(row=1, column=0, sticky="w", pady=5)
    entry_id = tk.Entry(frame, font=("Arial", 12), width=30)
    entry_id.grid(row=1, column=1, pady=5)

    tk.Label(frame, text="Password:", font=("Arial", 12), fg="white", bg="black").grid(row=2, column=0, sticky="w", pady=5)
    entry_password = tk.Entry(frame, font=("Arial", 12), width=30, show="*")
    entry_password.grid(row=2, column=1, pady=5)

    # Buttons
    btn_frame = tk.Frame(root, bg="lightblue")
    btn_frame.pack(pady=10)

    btn_login = tk.Button(btn_frame, text="Login", font=("Arial", 12), bg="red", fg="black", command=login)
    btn_login.grid(row=0, column=0, padx=20)

    btn_quit = tk.Button(btn_frame, text="Quit", font=("Arial", 12), bg="red", fg="black", command=root.destroy)
    btn_quit.grid(row=0, column=1, padx=20)

    root.mainloop()

if __name__ == "__main__":
    initialize_database()
    setup_login_gui()