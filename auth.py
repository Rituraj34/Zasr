class User:
    def __init__(self, username, full_name, role):
        self.username = username
        self.full_name = full_name
        self.role = role

def authenticate(username, password):
    try:
        with open("data/passwords.txt", "r") as file:
            for line in file:
                u, p, role = line.strip().split(",")
                if username == u and password == p:
                    return role
    except Exception as e:
        print("Error during authentication:", e)
    return None

def get_user_details(username):
    try:
        with open("data/user.txt", "r") as file:
            for line in file:
                u, name, role = line.strip().split(",")
                if u == username:
                    return User(u, name, role)
    except Exception as e:
        print("Error reading user details:", e)
    return None

# Student-only functions
def get_student_grades(username):
    try:
        with open("data/grades.txt", "r") as file:
            for line in file:
                u, *grades = line.strip().split(",")
                if u == username:
                    return grades
    except:
        return None

def get_student_eca(username):
    try:
        with open("data/eca.txt", "r") as file:
            for line in file:
                u, *activities = line.strip().split(",")
                if u == username:
                    return activities
    except:
        return None

def update_student_profile(username, new_name):
    try:
        updated_lines = []
        with open("data/users.txt", "r") as file:
            for line in file:
                u, name, role = line.strip().split(",")
                if u == username:
                    updated_lines.append(f"{u},{new_name},{role}\n")
                else:
                    updated_lines.append(line)
        with open("data/users.txt", "w") as file:
            file.writelines(updated_lines)
        return True
    except:
        return False