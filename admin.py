import tkinter as tk
from tkinter import messagebox

def admin_dashboard(user):
    def add_user():
        def submit():
            uname = entry_username.get()
            pwd = entry_password.get()
            role = entry_role.get()
            full_name = entry_full_name.get()

            with open("data/users.txt", "a") as ufile:
                ufile.write(f"{uname},{full_name},{role}\n")

            with open("data/passwords.txt", "a") as pfile:
                pfile.write(f"{uname},{pwd},{role}\n")

            messagebox.showinfo("Success", "User added successfully.")
            add_window.destroy()

        add_window = tk.Toplevel()
        add_window.title("Add User")
        add_window.geometry("300x300")

        tk.Label(add_window, text="Username").pack()
        entry_username = tk.Entry(add_window)
        entry_username.pack()

        tk.Label(add_window, text="Password").pack()
        entry_password = tk.Entry(add_window)
        entry_password.pack()

        tk.Label(add_window, text="Full Name").pack()
        entry_full_name = tk.Entry(add_window)
        entry_full_name.pack()

        tk.Label(add_window, text="Role (admin/student)").pack()
        entry_role = tk.Entry(add_window)
        entry_role.pack()

        tk.Button(add_window, text="Submit", command=submit).pack(pady=10)

    dashboard = tk.Toplevel()
    dashboard.title("Admin Dashboard")
    dashboard.geometry("400x300")

    tk.Label(dashboard, text=f"Welcome Admin: {user.full_name}", font=("Arial", 14)).pack(pady=10)
    tk.Button(dashboard, text="Add User", command=add_user).pack(pady=10)