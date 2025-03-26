
import sys
import os.path
from os import path

def main():
    login_controller()

def login_controller():
    admin_info = {"username": "admin", "password": "admin123"}
    
    while True:
        print("\n=== SUPERMARKET SYSTEM ===")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")
        
        selection = input("Select option (1-3): ")
        
        if selection == "1":
            authenticate_user(admin_info)
        elif selection == "2":
            register_account()
        elif selection == "3":
            sys.exit()
        else:
            print("Invalid selection!")

def authenticate_user(admin_creds):
    print("\n=== LOGIN ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    if len(username) == 0 or len(password) == 0:
        print("Credentials cannot be empty!")
        return
    
    if username == admin_creds["username"]:
        if password == admin_creds["password"]:
            print("\nWelcome Admin!")
            launch_admin_console()
        else:
            print("Incorrect admin password!")
    else:
        verify_customer(username, password)

def verify_customer(username, password):
    userfile = f"{username}.txt"
    if path.exists(userfile):
        with open(userfile, "r") as f:
            if f.read().split(",")[0] == password:
                print(f"\nWelcome {username}!")
                with open("currentuser.txt", "w") as f:
                    f.write(userfile)
                launch_customer_console()
            else:
                print("Incorrect password!")
    else:
        print("Account not found!")

def register_account():
    print("\n=== REGISTRATION ===")
    while True:
        new_user = input("New username: ").strip()
        if len(new_user) == 0:
            print("Username required!")
        else:
            break
    
    while True:
        new_pass = input("New password: ").strip()
        if len(new_pass) > 0:
            break
        print("Password required!")
    
    with open(f"{new_user}.txt", "w") as f:
        f.write(f"{new_pass},")
    print("Registration successful!")

def launch_admin_console():
    from admin import admin_interface
    admin_interface()

def launch_customer_console():
    from customer import customer_interface
    customer_interface()

if __name__ == "__main__":
    main()
