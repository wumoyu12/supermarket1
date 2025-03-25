import sys
import os.path
from os import path

def main():
    admin_interface()

def admin_interface():
    base_dir = os.path.dirname(os.path.realpath("__file__"))
    departments = ["Fruit", "Poultry", "Meat", "Beverage", "Frozenfood", "Dietfood", "Kosher", "Halal"]
    
    while True:
        print("\n=== ADMIN PANEL ===")
        print("1. View Products")
        print("2. Add Products")
        print("3. Clear Products") 
        print("4. Exit Admin")
        
        selection = input("Select option (1-4): ")
        
        if selection == "1":
            selected_dept = get_department_choice(departments)
            show_products(selected_dept)
        elif selection == "2":
            selected_dept = get_department_choice(departments)
            add_new_product(selected_dept)
        elif selection == "3":
            selected_dept = get_department_choice(departments)
            clear_department(selected_dept)
        elif selection == "4":
            print("Returning to login...")
            execute_script("login.py")
            return
        else:
            print("Invalid selection! Try again.")

def get_department_choice(department_list):
    while True:
        print("\nAvailable Departments:")
        count = 1
        while count <= len(department_list):
            print(f"{count}. {department_list[count-1]}")
            count += 1
        
        choice = input("Select department (1-8): ")
        if choice.isdigit():
            if int(choice) >= 1 and int(choice) <= 8:
                return department_list[int(choice)-1]
        print("Invalid department selection!")

def show_products(department):
    product_file = f"{department}.txt"
    price_file = f"price{department}.txt"
    
    if path.exists(product_file) == False:
        print(f"No products found in {department} department!")
        return
    
    with open(product_file, "r") as pf, open(price_file, "r") as prf:
        products = pf.read().split(",")
        prices = prf.read().split(",")
    
    print(f"\n{department.upper()} DEPARTMENT PRODUCTS:")
    idx = 1
    while idx <= len(products):
        if len(products[idx-1]) > 0:
            print(f"{idx}. {products[idx-1]} - ${prices[idx-1]}")
        idx += 1

def add_new_product(department):
    while True:
        product_name = input("\nEnter product name (or 'back' to return): ").strip()
        if product_name.lower() == 'back':
            return
        if len(product_name) > 0:
            break
        print("Product name cannot be empty!")
    
    while True:
        product_price = input("Enter product price: $")
        if validate_price(product_price):
            break
        print("Invalid price format! Use numbers like 5.99")
    
    with open(f"{department}.txt", "a") as pf, open(f"price{department}.txt", "a") as prf:
        pf.write(f"{product_name},")
        prf.write(f"{product_price},")
    
    print(f"Added {product_name} to {department} department!")

def validate_price(price):
    try:
        float(price)
        return True
    except ValueError:
        return False

def clear_department(department):
    confirm = input(f"WARNING: This will clear ALL {department} products. Continue? (y/n): ")
    if confirm.lower() == 'y':
        with open(f"{department}.txt", "w") as pf, open(f"price{department}.txt", "w") as prf:
            pf.write("")
            prf.write("")
        print(f"All {department} products cleared!")
    else:
        print("Operation cancelled.")

def execute_script(script_name):
    script_path = os.path.join(os.path.dirname(os.path.realpath("__file__")), script_name)
    exec_vars = {"__file__": script_path, "__name__": "__main__"}
    with open(script_path, "rb") as f:
        exec(compile(f.read(), script_path, "exec"), exec_vars)

if __name__ == "__main__":
    main()
