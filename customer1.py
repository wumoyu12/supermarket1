
import os.path
from os import path

def main():
    customer_interface()

def customer_interface():
    departments = ["Fruit", "Poultry", "Meat", "Beverage",
                  "Frozenfood", "Dietfood", "Kosher", "Halal"]
    
    while True:
        print("\n=== SHOPPING CONSOLE ===")
        print("1. Browse Departments")
        print("2. View Cart")
        print("3. Checkout")
        print("4. Logout")
        
        choice = input("Select option (1-4): ")
        
        if choice == "1":
            browse_departments(departments)
        elif choice == "2":
            view_cart()
        elif choice == "3":
            checkout()
        elif choice == "4":
            print("Logging out...")
            return
        else:
            print("Invalid selection!")

def browse_departments(dept_list):
    selected = select_department(dept_list)
    if selected is None:
        return
    
    print(f"\n=== {selected.upper()} PRODUCTS ===")
    display_products(selected)
    
    while True:
        print("\n1. Add to Cart")
        print("2. Back to Menu")
        action = input("Select action (1-2): ")
        
        if action == "1":
            add_to_cart(selected)
        elif action == "2":
            break
        else:
            print("Invalid action!")

def select_department(dept_list):
    print("\nAvailable Departments:")
    for i in range(len(dept_list)):
        print(f"{i+1}. {dept_list[i]}")
    
    sel = input("Select department (1-8): ")
    if sel.isdigit() and 1 <= int(sel) <= 8:
        return dept_list[int(sel)-1]
    print("Invalid selection!")
    return None

def display_products(department):
    prod_file = f"{department}.txt"
    price_file = f"price{department}.txt"
    
    if path.exists(prod_file) == False:
        print("No products available!")
        return
    
    with open(prod_file, "r") as pf, open(price_file, "r") as prf:
        products = pf.read().split(",")
        prices = prf.read().split(",")
    
    print("\nAvailable Items:")
    for i in range(len(products)):
        if len(products[i]) > 0:
            print(f"{i+1}. {products[i]} - ${prices[i]}")

def add_to_cart(department):
    prod_file = f"{department}.txt"
    price_file = f"price{department}.txt"
    
    with open(prod_file, "r") as pf, open(price_file, "r") as prf:
        products = pf.read().split(",")
        prices = prf.read().split(",")
    
    while True:
        sel = input("Enter product number: ")
        if sel.isdigit() and 1 <= int(sel) <= len(products):
            break
        print("Invalid selection!")
    
    while True:
        qty = input("Enter quantity: ")
        if qty.isdigit() and int(qty) > 0:
            break
        print("Invalid quantity!")
    
    selected = products[int(sel)-1]
    price = prices[int(sel)-1]
    total = float(price) * int(qty)
    
    with open("currentuser.txt", "r") as f:
        userfile = f.read()
    
    with open(userfile, "a") as f:
        f.write(f"{selected},{price},{qty},{total},")
    
    print(f"Added {qty}x {selected} to cart!")

def view_cart():
    with open("currentuser.txt", "r") as f:
        userfile = f.read()
    
    if path.exists(userfile) == False:
        print("Your cart is empty!")
        return
    
    with open(userfile, "r") as f:
        items = f.read().split(",")
    
    print("\n=== YOUR CART ===")
    total = 0.0
    i = 0
    while i < len(items)-3:
        if len(items[i]) > 0:
            print(f"{items[i]} - ${items[i+1]} x {items[i+2]} = ${items[i+3]}")
            total += float(items[i+3])
            i += 4
        else:
            i += 1
    
    print(f"\nTOTAL: ${total:.2f}")

def checkout():
    view_cart()
    confirm = input("\nConfirm purchase? (y/n): ")
    if confirm.lower() == "y":
        with open("currentuser.txt", "r") as f:
            userfile = f.read()
        with open(userfile, "w") as f:
            f.write("")
        print("Purchase completed! Thank you!")
    else:
        print("Checkout cancelled.")

if __name__ == "__main__":
    main()
