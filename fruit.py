import sys
import os.path
from os import path

def main():
    fruit_department()

def fruit_department():
    dept_name = "Fruit"
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    
    with open("currentuser.txt", "r") as f:
        username = f.read().split(".")[0]
    
    print(f"\nWelcome to {dept_name} Department, {username}!")
    
    while True:
        try:
            with open("Fruit.txt", "r") as f, open("priceFruit.txt", "r") as pf:
                fruits = f.read().split(",")
                prices = pf.read().split(",")
        except:
            fruits = []
            prices = []
        
        if not fruits:
            print("\nNo fruits available currently.")
        else:
            print("\nAvailable Fruits:")
            for i, (fruit, price) in enumerate(zip(fruits, prices), 1):
                if fruit:
                    print(f"{i}. {fruit} - ${price}")
        
        print("\n1. Select Fruit")
        print("2. Back to Departments")
        print("3. View Cart")
        print("4. Logout")
        
        choice = input("Choose option (1-4): ")
        
        if choice == "1":
            if not fruits:
                print("No fruits to select!")
                continue
                
            while True:
                fruit_num = input("Enter fruit number: ")
                if fruit_num.isdigit() and 1 <= int(fruit_num) <= len(fruits):
                    break
                print("Invalid selection!")
            
            selected_fruit = fruits[int(fruit_num)-1]
            selected_price = prices[int(fruit_num)-1]
            
            while True:
                quantity = input(f"How many {selected_fruit}? ")
                if quantity.isdigit() and int(quantity) > 0:
                    break
                print("Invalid quantity!")
            
            add_to_cart(selected_fruit, selected_price, quantity)
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
