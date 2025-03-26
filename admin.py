import sys
import os.path
from os import path

def main():
    admin_interface()

def admin_interface():
    departments = ["Fruit", "Poultry", "Meat", "Beverage", 
                  "Frozenfood", "Dietfood", "Kosher", "Halal"]
    
    while True:
        print("\n=== ADMIN CONSOLE ===")
        print("1. Manage Products")
        print("2. View Departments")
        print("3. Logout")
        
        choice = input("Select option (1-3): ")
        
        if choice == "1":
            manage_products(departments)
        elif choice == "2":
            view_departments(departments)
        elif choice == "3":
            print("Logging out...")
            return
        else:
            print("Invalid input!")

def manage_products(dept_list):
    selected = select_department(dept_list)
    if selected is None:
        return
    
    print(f"\n=== {selected.upper()} MANAGEMENT ===")
    print("1. Add Product")
    print("2. View Products")
    print("3. Clear Products")
    
    action = input("Select action (1-3): ")
    
    if action == "1":
        add_product(selected)
    elif action == "2":
        display_products(selected)
    elif action == "3":
        reset_products(selected)
    else:
        print("Invalid action!")

def select_department(dept_list):
    print("\nAvailable Departments:")
    i = 0
    while i < len(dept_list):
        print(f"{i+1}. {dept_list[i]}")
        i += 1
    
    sel = input("Select department (1-8): ")
    if sel.isdigit() and 1 <= int(sel) <= 8:
        return dept_list[int(sel)-1]
    print("Invalid selection!")
    return None

def add_product(department):
    while True:
        name = input("Product name: ").strip()
        if len(name) > 0:
            break
        print("Name required!")
    
    while True:
        price = input("Price: $")
        if validate_price(price):
            break
        print("Invalid price format!")
    
    with open(f"{department}.txt", "a") as f:
        f.write(f"{name},")
    with open(f"price{department}.txt", "a") as f:
        f.write(f"{price},")
    print(f"Added {name} to {department}!")

def validate_price(price):
    dot_count = 0
    for char in price:
        if char == ".":
            dot_count += 1
        elif char < "0" or char > "9":
            return False
    return dot_count <= 1 and len(price) > 0

def display_products(department):
    prod_file = f"{department}.txt"
    price_file = f"price{department}.txt"
    
    if path.exists(prod_file) == False:
        print("No products found!")
        return
    
    with open(prod_file, "r") as pf, open(price_file, "r") as prf:
        products = pf.read().split(",")
        prices = prf.read().split(",")
    
    print("\nCurrent Products:")
    i = 0
    while i < len(products):
        if len(products[i]) > 0:
            print(f"{i+1}. {products[i]} - ${prices[i]}")
        i += 1

def reset_products(department):
    confirm = input(f"Clear ALL {department} products? (y/n): ")
    if confirm.lower() == "y":
        with open(f"{department}.txt", "w") as f1, open(f"price{department}.txt", "w") as f2:
            f1.write("")
            f2.write("")
        print("Products cleared!")
    else:
        print("Operation cancelled.")

def view_departments(dept_list):
    print("\n=== DEPARTMENTS ===")
    for i in range(len(dept_list)):
        print(f"{i+1}. {dept_list[i]}")

if __name__ == "__main__":
    main()
