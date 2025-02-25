# remove_student.py
import tkinter as tk
from tkinter import messagebox
from database import conn, cursor, refresh_table

def remove_student(entry_id, tree):
    student_id = entry_id.get()
    
    if student_id:
        cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
        student = cursor.fetchone()
        
        if student:
            cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
            conn.commit()
            messagebox.showinfo("Success", f"Student ID {student_id} deleted successfully!")
            entry_id.delete(0, tk.END)
            refresh_table(tree)
        else:
            messagebox.showerror("Error", "Student ID not found!")
    else:
        messagebox.showerror("Error", "Please enter a Student ID!")

def open_remove_student_window(tree):
    remove_window = tk.Toplevel()
    remove_window.title("Remove Student")
    remove_window.geometry("400x200")
    remove_window.configure(bg="lightblue")

    tk.Label(remove_window, text="Remove Student", font=("Arial", 14, "bold"), bg="lightblue").pack(pady=10)

    tk.Label(remove_window, text="Student ID:", font=("Arial", 12), bg="lightblue").pack(pady=5)
    entry_id = tk.Entry(remove_window, font=("Arial", 12), width=30)
    entry_id.pack(pady=5)

    btn_remove = tk.Button(remove_window, text="Remove Student", font=("Arial", 12), bg="red", fg="black", command=lambda: remove_student(entry_id, tree))
    btn_remove.pack(pady=10)