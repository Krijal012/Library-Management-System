# librarian_login.py
import tkinter as tk
from tkinter import messagebox
import subprocess

# Predefined Librarian credentials
librarian_credentials = {
    "240576": "prashanna",
    "240421": "suyes",
    "240399": "reshav"
}

def librarian_login():
    user_id = entry_id.get().strip()
    password = entry_password.get().strip()
    
    if user_id in librarian_credentials and librarian_credentials[user_id] == password:
        subprocess.run(["python", "librariandashboard.py"])
    else:
        messagebox.showerror("Error", "Invalid ID or Password!")

# GUI setup
root = tk.Tk()
root.title("Librarian Login")
root.geometry("400x300")
root.configure(bg="lightblue")

frame = tk.Frame(root, bg="black", padx=10, pady=10)
frame.pack(pady=20)

tk.Label(root, text="Librarian Login", font=("Arial", 14, "bold"), bg="lightblue").pack()

# Labels and entry fields
tk.Label(frame, text="User ID:", font=("Arial", 12), fg="white", bg="black").grid(row=0, column=0, sticky="w", pady=5)
entry_id = tk.Entry(frame, font=("Arial", 12), width=30)
entry_id.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Password:", font=("Arial", 12), fg="white", bg="black").grid(row=1, column=0, sticky="w", pady=5)
entry_password = tk.Entry(frame, font=("Arial", 12), width=30, show="*")
entry_password.grid(row=1, column=1, pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="lightblue")
btn_frame.pack(pady=10)

btn_login = tk.Button(btn_frame, text="Login", font=("Arial", 12), bg="red", fg="black", command=librarian_login)
btn_login.grid(row=0, column=0, padx=20)

btn_quit = tk.Button(btn_frame, text="Quit", font=("Arial", 12), bg="red", fg="black", command=root.destroy)
btn_quit.grid(row=0, column=1, padx=20)

root.mainloop()