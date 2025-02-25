# add_student.py
import tkinter as tk
from tkinter import messagebox
import sqlite3
from database import conn, cursor, refresh_table

def add_student(entry_id, entry_name, tree):
    student_id = entry_id.get()
    student_name = entry_name.get()
    
    if student_id and student_name:
        try:
            cursor.execute("INSERT INTO students VALUES (?, ?)", (student_id, student_name))
            conn.commit()
            messagebox.showinfo("Success", "Student added successfully!")
            entry_id.delete(0, tk.END)
            entry_name.delete(0, tk.END)
            refresh_table(tree)
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Student ID already exists!")
    else:
        messagebox.showerror("Error", "All fields are required!")

def open_add_student_window(tree):
    add_window = tk.Toplevel()
    add_window.title("Add Student")
    add_window.geometry("400x300")
    add_window.configure(bg="lightblue")

    tk.Label(add_window, text="Add Student", font=("Arial", 14, "bold"), bg="lightblue").pack(pady=10)

    tk.Label(add_window, text="Student ID:", font=("Arial", 12), bg="lightblue").pack(pady=5)
    entry_id = tk.Entry(add_window, font=("Arial", 12), width=30)
    entry_id.pack(pady=5)

    tk.Label(add_window, text="Student Name:", font=("Arial", 12), bg="lightblue").pack(pady=5)
    entry_name = tk.Entry(add_window, font=("Arial", 12), width=30)
    entry_name.pack(pady=5)

    btn_add = tk.Button(add_window, text="Add Student", font=("Arial", 12), bg="red", fg="black", command=lambda: add_student(entry_id, entry_name, tree))
    btn_add.pack(pady=10)