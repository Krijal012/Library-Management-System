import tkinter as tk
from add_book import open_add_book_window
from remove_book import open_remove_book_window

# GUI setup
root = tk.Tk()
root.title("Librarian Dashboard")
root.geometry("800x600")
root.configure(bg="lightblue")

tk.Label(root, text="Librarian Dashboard", font=("Arial", 14, "bold"), bg="lightblue").pack(pady=10)

# Add Book Button
btn_add_book = tk.Button(root, text="Add Book", font=("Arial", 12), bg="red", fg="black", command=open_add_book_window)
btn_add_book.pack(pady=10)

# Remove Book Button
btn_remove_book = tk.Button(root, text="Remove Book", font=("Arial", 12), bg="red", fg="black", command=open_remove_book_window)
btn_remove_book.pack(pady=10)

root.mainloop()
