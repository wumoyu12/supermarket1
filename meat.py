import sys
import os.path
from os import path

def main():
    meat_department()

def meat_department():
    dept_name = "Meat"
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    
    with open("currentuser.txt", "r") as f:
        username = f.read().split(".")[0]
    
    print(f"\nWelcome to {dept_name} Department, {username}!")
    
    while True:
        try:
            with open("Meat.txt", "r") as f, open("priceMeat.txt", "r") as pf:
                meats = f.read().split(",")
                prices = pf.read().split(",")
        except:
            meats = []
            prices = []
        
        if not meats:
            print("\nNo meat products available currently.")
        else:
            print("\nAvailable Meats:")
            for i, (meat, price) in enumerate(zip(meats, prices), 1):
                if meat:
                    print(f"{i}. {meat} - ${price}")
        
        print("\n1. Select Meat")
        print("2. Back to Departments")
        print("3. View Cart")
        print("4. Logout")
        
        choice = input("Choose option (1-4): ")
        
        if choice == "1":
            if not meats:
                print("No meats to select!")
                continue
                
            while True:
                meat_num = input("Enter meat number: ")
                if meat_num.isdigit() and 1 <= int(meat_num) <= len(meats):
                    break
                print("Invalid selection!")
            
            selected_meat = meats[int(meat_num)-1]
            selected_price = prices[int(meat_num)-1]
            
            while True:
                quantity = input(f"How many {selected_meat}? ")
                if quantity.isdigit() and int(quantity) > 0:
                    break
                print("Invalid quantity!")
            
            add_to_cart(selected_meat, selected_price, quantity)
        elif choice == "2":
            run_script("customer.py")
            break
        elif choice == "3":
            run_script("receipt.py")
            break
        elif choice == "4":
            print("Logging out...")
            run_script("login.py")
            break
        else:
            print("Invalid choice!")

def add_to_cart(item, price, qty):
    total = float(price) * int(qty)
    with open("currentuser.txt", "r") as f:
        userfile = f.read()
    with open(userfile, "a") as f:
        f.write(f"{item},{price},{qty},{total},")
    print(f"Added {qty}x {item} to cart!")

def run_script(script):
    filepath = os.path.join(os.path.dirname(os.path.realpath("__file__")), script)
    exec_vars = {"__file__": filepath, "__name__": "__main__"}
    with open(filepath, "rb") as f:
        exec(compile(f.read(), filepath, "exec"), exec_vars)

if __name__ == "__main__":
    main()
