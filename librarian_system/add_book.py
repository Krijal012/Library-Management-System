import tkinter as tk
from tkinter import messagebox
import sqlite3
from database import get_db_connection

def add_book():
    conn, cursor = get_db_connection()
    
    book_id = entry_book_id.get()
    title = entry_title.get()
    author = entry_author.get()
    isbn = entry_isbn.get()
    
    if book_id and title and author and isbn:
        try:
            cursor.execute("INSERT INTO books VALUES (?, ?, ?, ?)", (book_id, title, author, isbn))
            conn.commit()
            messagebox.showinfo("Success", "Book added successfully!")
            entry_book_id.delete(0, tk.END)
            entry_title.delete(0, tk.END)
            entry_author.delete(0, tk.END)
            entry_isbn.delete(0, tk.END)
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Book ID already exists!")
    else:
        messagebox.showerror("Error", "All fields are required!")

def open_add_book_window():
    add_window = tk.Toplevel()
    add_window.title("Add Book")
    add_window.geometry("400x300")
    add_window.configure(bg="lightblue")

    global entry_book_id, entry_title, entry_author, entry_isbn

    tk.Label(add_window, text="Add Book", font=("Arial", 14, "bold"), bg="lightblue").pack(pady=10)

    tk.Label(add_window, text="Book ID:", font=("Arial", 12), bg="lightblue").pack(pady=5)
    entry_book_id = tk.Entry(add_window, font=("Arial", 12), width=30)
    entry_book_id.pack(pady=5)

    tk.Label(add_window, text="Title:", font=("Arial", 12), bg="lightblue").pack(pady=5)
    entry_title = tk.Entry(add_window, font=("Arial", 12), width=30)
    entry_title.pack(pady=5)

    tk.Label(add_window, text="Author:", font=("Arial", 12), bg="lightblue").pack(pady=5)
    entry_author = tk.Entry(add_window, font=("Arial", 12), width=30)
    entry_author.pack(pady=5)

    tk.Label(add_window, text="ISBN:", font=("Arial", 12), bg="lightblue").pack(pady=5)
    entry_isbn = tk.Entry(add_window, font=("Arial", 12), width=30)
    entry_isbn.pack(pady=5)

    btn_add = tk.Button(add_window, text="Add Book", font=("Arial", 12), bg="red", fg="black", command=add_book)
    btn_add.pack(pady=10)