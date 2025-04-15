import tkinter as tk
from tkinter import messagebox
from auth import authenticate, get_user_details, add_user, delete_user, get_student_grades, get_student_eca, update_student_profile



# Read users from student.txt
def load_users_from_file():
    users = {}
    try:
        with open("student.txt", "r") as f:
            for line in f:
                data = line.strip().split(",")
                if len(data) >= 3:
                    username, password, name = data[0], data[1], data[2]
                    users[username] = {
                        "password": password,
                        "name": name,
                        "grade": data[3] if len(data) > 3 else "",
                        "eca": data[4] if len(data) > 4 else ""
                    }
    except FileNotFoundError:
        messagebox.showerror("File Not Found", "The file 'student.txt' was not found.")
    return users

# Authenticate user
def authenticate(username, password, users):
    return username in users and users[username]["password"] == password

# Get user details
def get_user_details(username, users):
    return users.get(username)

def login():
    username = userNameEntry.get()
    password = userPasswordEntry.get()
    users = load_users_from_file()

    if authenticate(username, password, users):
        messagebox.showinfo("Login Successful", "Welcome to the system!")
        user_details = get_user_details(username, users)
        print("User Details:", user_details)  # You can use this to show other info
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def main():
    window = tk.Tk()
    window.title("Login")
    window.geometry("400x350")
    window.configure(bg="#e0f7fa")

    frame = tk.Frame(window, bg="white", bd=2, relief="ridge", padx=20, pady=20)
    frame.place(relx=0.5, rely=0.5, anchor="center")

    title = tk.Label(frame, text="Login", font=("Helvetica", 18, "bold"), bg="white", fg="#333")
    title.pack(pady=(0, 20))

    userName = tk.Label(frame, text="Username", font=("Arial", 12), bg="white")
    userName.pack(anchor="w")
    global userNameEntry
    userNameEntry = tk.Entry(frame, font=("Arial", 12), width=30, bd=1, relief="solid")
    userNameEntry.pack(pady=(5, 15))

    userPassword = tk.Label(frame, text="Password", font=("Arial", 12), bg="white")
    userPassword.pack(anchor="w")
    global userPasswordEntry
    userPasswordEntry = tk.Entry(frame, show="*", font=("Arial", 12), width=30, bd=1, relief="solid")
    userPasswordEntry.pack(pady=(5, 20))

    global loginBtn
    loginBtn = tk.Button(frame, text="Login", font=("Arial", 12, "bold"),
                         bg="#4CAF50", fg="white", width=25, pady=5, command=login)
    loginBtn.pack()

    window.mainloop()

if __name__ == "__main__":
    main()