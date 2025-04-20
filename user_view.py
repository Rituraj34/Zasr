import tkinter as tk
from tkinter import messagebox
from auth import authenticate, get_user_details
from admin import admin_dashboard
from student import student_dashboard

def login():
    username = username_entry.get()
    password = password_entry.get()
    
    role = authenticate(username, password)  # Get the role from passwords.txt
    if role:
        user = get_user_details(username)
        if not user:
            messagebox.showerror("Error", "User details not found.")
            return

        messagebox.showinfo("Login Successful", f"Welcome, {user.full_name}!")

        if role == "admin":
            admin_dashboard(user)
        elif role == "student":
            student_dashboard(user)
        else:
            messagebox.showerror("Error", "Unknown role.")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def main():
    global username_entry, password_entry

    root = tk.Tk()
    root.title("Student Profile Management System")
    root.geometry("400x300")

    frame = tk.Frame(root)
    frame.pack(expand=True)

    tk.Label(frame, text="Username:").pack(pady=5)
    username_entry = tk.Entry(frame)
    username_entry.pack(pady=5)

    tk.Label(frame, text="Password:").pack(pady=5)
    password_entry = tk.Entry(frame, show="*")
    password_entry.pack(pady=5)

    tk.Button(frame, text="Login", command=login).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()