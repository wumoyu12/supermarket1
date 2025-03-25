import sys
import os.path
from os import path

def main():
    halal_department()

def halal_department():
    dept_name = "Halal"
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    
    with open("currentuser.txt", "r") as f:
        username = f.read().split(".")[0]
    
    print(f"\nWelcome to {dept_name} Department, {username}!")
    
    while True:
        try:
            with open("Halal.txt", "r") as f, open("priceHalal.txt", "r") as pf:
                halal_items = f.read().split(",")
                prices = pf.read().split(",")
        except:
            halal_items = []
            prices = []
        
        if not halal_items:
            print("\nNo halal items available currently.")
        else:
            print("\nAvailable Halal Items:")
            for i, (item, price) in enumerate(zip(halal_items, prices), 1):
                if item:
                    print(f"{i}. {item} - ${price}")
        
        print("\n1. Select Halal Item")
        print("2. Back to Departments")
        print("3. View Cart")
        print("4. Logout")
        
        choice = input("Choose option (1-4): ")
        
        if choice == "1":
            if not halal_items:
                print("No items to select!")
                continue
                
            while True:
                item_num = input("Enter item number: ")
                if item_num.isdigit() and 1 <= int(item_num) <= len(halal_items):
                    break
                print("Invalid selection!")
            
            selected_item = halal_items[int(item_num)-1]
            selected_price = prices[int(item_num)-1]
            
            while True:
                quantity = input(f"How many {selected_item}? ")
                if quantity.isdigit() and int(quantity) > 0:
                    break
                print("Invalid quantity!")
            
            add_to_cart(selected_item, selected_price, quantity)
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
