import sys
import os.path
from os import path

def main():
    login_screen()

def login_screen():
    admin_user = "admin"
    admin_pass = "adminpassword"
    
    while True:
        print("\n=== SUPERMARKET SYSTEM ===")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")
        
        choice = input("Enter choice (1-3): ")
        
        if choice == "1":
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            
            if len(username) == 0 or len(password) == 0:
                print("Username and password required!")
            else:
                if username == admin_user:
                    if password == admin_pass:
                        print("\nWelcome Admin!")
                        run_admin_panel()
                        return
                    else:
                        print("Incorrect admin password!")
                else:
                    check_customer_login(username, password)
        elif choice == "2":
            create_new_account()
        elif choice == "3":
            sys.exit()
        else:
            print("Invalid choice!")

def check_customer_login(username, password):
    userfile = f"{username}.txt"
    if path.exists(userfile):
        with open(userfile, "r") as f:
            stored_pass = f.read().split(",")[0]
            if stored_pass == password:
                print(f"\nWelcome {username}!")
                with open("currentuser.txt", "w") as f:
                    f.write(userfile)
                run_customer_panel()
                return
            else:
                print("Incorrect password!")
    else:
        print("User not found!")

def create_new_account():
    while True:
        new_user = input("New username: ").strip()
        if len(new_user) == 0:
            print("Username cannot be empty!")
        else:
            if path.exists(f"{new_user}.txt"):
                print("Username already exists!")
            else:
                break
    
    while True:
        new_pass = input("New password: ").strip()
        if len(new_pass) > 0:
            break
        print("Password cannot be empty!")
    
    with open(f"{new_user}.txt", "w") as f:
        f.write(f"{new_pass},")
    print("Account created! Please login.")

def run_admin_panel():
    from admin import admin_interface
    admin_interface()

def run_customer_panel():
    from customer import customer_shopping
    customer_shopping()

if __name__ == "__main__":
    main()
