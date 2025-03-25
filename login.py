import sys
import os.path
from os import path

def main():
    user_login()

def user_login():
    admin_credentials = {"username": "admin", "password": "admin123"}
    base_dir = os.path.dirname(os.path.realpath("__file__"))
    
    while True:
        print("\n=== SUPERMARKET SYSTEM ===")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")
        
        initial_choice = input("Select option (1-3): ")
        
        if initial_choice == "1":
            handle_login(admin_credentials)
        elif initial_choice == "2":
            create_new_account()
        elif initial_choice == "3":
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid selection!")

def handle_login(admin_creds):
    while True:
        print("\n=== LOGIN ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()
        
        if not username or not password:
            print("Username and password required!")
            continue
        
        if username == admin_creds["username"]:
            if password == admin_creds["password"]:
                print("\nAdmin login successful!")
                execute_script("admin.py")
                return
            else:
                print("Incorrect admin password!")
                return
        
        user_file = f"{username}.txt"
        if path.exists(user_file):
            with open(user_file, "r") as f:
                if f.read().split(",")[0] == password:
                    print(f"\nWelcome {username}!")
                    with open("currentuser.txt", "w") as cu:
                        cu.write(user_file)
                    execute_script("customer.py")
                    return
                else:
                    print("Incorrect password!")
                    return
        else:
            print("User not found!")
            return

def create_new_account():
    while True:
        print("\n=== CREATE ACCOUNT ===")
        new_user = input("Choose username: ").strip()
        
        if not new_user:
            print("Username cannot be empty!")
            continue
            
        if path.exists(f"{new_user}.txt"):
            print("Username already exists!")
            continue
            
        new_pass = input("Choose password: ").strip()
        if not new_pass:
            print("Password cannot be empty!")
            continue
            
        with open(f"{new_user}.txt", "w") as f:
            f.write(f"{new_pass},")
        
        print("Account created successfully! Please login.")
        return

def execute_script(script_name):
    script_path = os.path.join(os.path.dirname(os.path.realpath("__file__")), script_name)
    exec_vars = {"__file__": script_path, "__name__": "__main__"}
    with open(script_path, "rb") as f:
        exec(compile(f.read(), script_path, "exec"), exec_vars)

if __name__ == "__main__":
    main()
