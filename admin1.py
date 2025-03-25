
import sys
import os.path
from os import path

def main():
    admin_panel()

def admin_panel():
    fileDir = os.path.dirname(os.path.realpath("__file__"))
    departments = ["Fruit", "Poultry", "Meat", "Beverage", "Frozenfood", "Dietfood", "Kosher", "Halal"]
    
    while True:
        print("\nAdmin Panel")
        print("1) View Products")
        print("2) Add Product")
        print("3) Clear all Products")
        print("4) Log Out")

        choice = str(input("Select an option (1-4): "))
        
        if choice == "1":
            dep = choose_department(departments)
            status_view(dep)
        elif choice == "2":
            dep = choose_department(departments)
            add_product(dep)
        elif choice == "3":
            dep = choose_department(departments)
            remove_product(dep)
        elif choice == "4":
            print("You have been logged out!")
            run_script("loginscreen.py")
            return
        else:
            print("Invalid input!")

def choose_department(departments):
    while True:
        i = 1
        while i <= len(departments):
            print(f"{i}) {departments[i-1]}")
            i += 1
        
        sel = input("Select department (1-8): ")
        if len(sel) == 1 and sel >= "1" and sel <= "8":
            return departments[int(sel)-1]
        print("Invalid selection!")

def status_view(dep):
    filename = f"{dep}.txt"
    if path.exists(filename) == False:
        print("No products available!")
        return

    with open(filename, "r") as f:
        products = f.read().split(",")
    
    with open(f"price{dep}.txt", "r") as f:
        prices = f.read().split(",")
    
    print(f"\n{dep} Department Products:")
    i = 1
    while i <= len(products):
        if len(products[i-1]) > 0:
            print(f"{i}) {products[i-1]} - ${prices[i-1]}")
        i += 1

def add_product(dep):
    while True:
        product = input("Enter product name: ").strip()
        if len(product) > 0:
            break
        print("Invalid name!")
    
    while True:
        price = input("Enter price: ")
        if check_price(price):
            break
        print("Invalid price!")
    
    with open(f"{dep}.txt", "a") as f:
        f.write(f"{product},")
    with open(f"price{dep}.txt", "a") as f:
        f.write(f"{price},")
    
    print(f"Added {product} to {dep}!")

def check_price(cost):
    decimalcount = 0
    valid = 0
    i = 0
    while i < len(cost):
        char = cost[i]
        if char >= "0" and char <= "9":
            valid = valid + 0
        elif char == ".":
            decimalcount = decimalcount + 1
        else:
            valid = valid + 1
        i += 1
    
    if len(cost) == 0 or cost == "0":
        valid = valid + 1
    
    return valid == 0 and decimalcount <= 1

def remove_product(dep):
    with open(f"{dep}.txt", "w") as f:
        f.write("")
    with open(f"price{dep}.txt", "w") as f:
        f.write("")
    print(f"Cleared all {dep} products!")

def run_script(script):
    filepath = os.path.join(os.path.dirname(os.path.realpath("__file__")), script)
    with open(filepath, "rb") as f:
        exec(compile(f.read(), filepath, "exec"), {"__file__": filepath, "__name__": "__main__"})

if __name__ == "__main__":
    main()
