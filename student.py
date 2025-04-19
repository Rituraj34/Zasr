import tkinter as tk
from tkinter import messagebox
from auth import get_student_grades, get_student_eca, update_student_profile



def student_dashboard(user):
    def view_details():
        grades = get_student_grades(user.username)
        eca = get_student_eca(user.username)

        win = tk.Toplevel()
        win.title("Student Details")
        win.geometry("400x400")

        tk.Label(win, text=f"Name: {user.full_name}").pack(pady=5)
        tk.Label(win, text=f"Role: {user.role}").pack(pady=5)

        tk.Label(win, text="Grades").pack()
        if grades:
            for i, g in enumerate(grades):
                tk.Label(win, text=f"Subject {i+1}: {g}").pack()
        else:
            tk.Label(win, text="No grades found").pack()

        tk.Label(win, text="Activities").pack()
        if eca:
            for act in eca:
                tk.Label(win, text=act).pack()
        else:
            tk.Label(win, text="No activities found").pack()

    def update_profile():
        def submit():
            new_name = entry.get()
            if update_student_profile(user.username, new_name):
                messagebox.showinfo("Success", "Updated successfully!")
                update_win.destroy()
            else:
                messagebox.showerror("Error", "Failed to update.")

        update_win = tk.Toplevel()
        update_win.title("Update Profile")
        update_win.geometry("300x200")

        entry = tk.Entry(update_win)
        entry.insert(0, user.full_name)
        entry.pack(pady=10)

        tk.Button(update_win, text="Submit", command=submit).pack()

    win = tk.Toplevel()
    win.title("Student Dashboard")
    win.geometry("400x300")

    tk.Label(win, text=f"Welcome, {user.full_name}!", font=("Arial", 16)).pack(pady=10)
    tk.Button(win, text="View Details", command=view_details).pack(pady=5)
    tk.Button(win, text="Update Profile", command=update_profile).pack(pady=5)
