# main.py
import tkinter as tk
from tkinter import ttk
from database import initialize_database, refresh_table
from add_student import open_add_student_window
from remove_student import open_remove_student_window

# Initialize the database
initialize_database()

# GUI setup
root = tk.Tk()
root.title("Admin Dashboard")
root.geometry("800x600")
root.configure(bg="lightblue")

tk.Label(root, text="Admin Dashboard", font=("Arial", 14, "bold"), bg="lightblue").pack(pady=10)

# Table Frame
frame = tk.Frame(root, bg="black", padx=5, pady=5)
frame.pack(pady=10)

# Treeview widget for displaying student records
tree = ttk.Treeview(frame, columns=("ID", "Name"), show="headings", height=10)
tree.heading("ID", text="ID")
tree.heading("Name", text="Name")
tree.column("ID", width=100, anchor="center")
tree.column("Name", width=200, anchor="center")
tree.pack()

# Refresh table on startup
refresh_table(tree)

# Buttons Frame
buttons_frame = tk.Frame(root, bg="lightblue")
buttons_frame.pack(pady=10)

btn_add = tk.Button(buttons_frame, text="Add Student", font=("Arial", 12), bg="red", fg="black", command=lambda: open_add_student_window(tree))
btn_add.pack(side=tk.LEFT, padx=10)

btn_remove = tk.Button(buttons_frame, text="Remove Student", font=("Arial", 12), bg="red", fg="black", command=lambda: open_remove_student_window(tree))
btn_remove.pack(side=tk.LEFT, padx=10)

root.mainloop()