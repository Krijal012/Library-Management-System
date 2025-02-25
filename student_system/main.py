# main.py
import tkinter as tk
from tkinter import ttk
from database import initialize_database, fetch_books, close_connection

# Initialize the database
initialize_database()

# GUI setup
root = tk.Tk()
root.title("Student Dashboard")
root.geometry("800x600")
root.configure(bg="lightblue")

tk.Label(root, text="Student Dashboard", font=("Arial", 14, "bold"), bg="lightblue").pack(pady=10)

# Table Frame
frame = tk.Frame(root, bg="black", padx=5, pady=5)
frame.pack(pady=10)

# Treeview widget for displaying book records
tree = ttk.Treeview(frame, columns=("Book ID", "Title", "Author", "ISBN"), show="headings", height=10)
tree.heading("Book ID", text="Book ID")
tree.heading("Title", text="Title")
tree.heading("Author", text="Author")
tree.heading("ISBN", text="ISBN")
tree.column("Book ID", width=100, anchor="center")
tree.column("Title", width=200, anchor="center")
tree.column("Author", width=200, anchor="center")
tree.column("ISBN", width=150, anchor="center")
tree.pack()

# Fetch books from database
books = fetch_books()

# Insert data into Treeview
for book in books:
    tree.insert("", tk.END, values=book)

# Close the database connection when the application is closed
def on_closing():
    close_connection()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()