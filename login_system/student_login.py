# student_login.py
import tkinter as tk
from tkinter import messagebox
import subprocess

# Predefined Student password
student_password = "student123"

def student_login():
    password = entry_password.get().strip()
    
    if password == student_password:
        subprocess.run(["python", "studentdashboard.py"])
    else:
        messagebox.showerror("Error", "Invalid Password!")

# GUI setup
root = tk.Tk()
root.title("Student Login")
root.geometry("400x300")
root.configure(bg="lightblue")

frame = tk.Frame(root, bg="black", padx=10, pady=10)
frame.pack(pady=20)

tk.Label(root, text="Student Login", font=("Arial", 14, "bold"), bg="lightblue").pack()

# Labels and entry fields
tk.Label(frame, text="Password:", font=("Arial", 12), fg="white", bg="black").grid(row=0, column=0, sticky="w", pady=5)
entry_password = tk.Entry(frame, font=("Arial", 12), width=30, show="*")
entry_password.grid(row=0, column=1, pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="lightblue")
btn_frame.pack(pady=10)

btn_login = tk.Button(btn_frame, text="Login", font=("Arial", 12), bg="red", fg="black", command=student_login)
btn_login.grid(row=0, column=0, padx=20)

btn_quit = tk.Button(btn_frame, text="Quit", font=("Arial", 12), bg="red", fg="black", command=root.destroy)
btn_quit.grid(row=0, column=1, padx=20)

root.mainloop()