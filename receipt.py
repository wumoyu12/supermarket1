import sys
import os.path
from os import path

def main():
    display_receipt()

def display_receipt():
    with open("userinfomessage.txt", "r") as f:
        user_file = f.read()
    
    with open(user_file, "r") as f:
        purchase_data = f.read().split(",")
    
    print("\n=== YOUR RECEIPT ===")
    print("Items Purchased:")
    total = 0.0
    item_count = 1
    
    for i in range(0, len(purchase_data)-3, 4):
        if purchase_data[i]:
            product = purchase_data[i]
            price = float(purchase_data[i+1])
            qty = int(purchase_data[i+2])
            subtotal = float(purchase_data[i+3])
            
            print(f"\n{item_count}. {product}")
            print(f"   Price: ${price:.2f} x {qty} = ${subtotal:.2f}")
            total += subtotal
            item_count += 1
    
    print("\n" + "="*30)
    print(f"TOTAL: ${total:.2f}")
    print("="*30)
    
    while True:
        print("\n1. Continue Shopping")
        print("2. Complete Purchase")
        print("3. Logout")
        
        option = input("Select option (1-3): ")
        
        if option == "1":
            execute_script("customer.py")
            break
        elif option == "2":
            print("Purchase completed! Thank you!")
            with open(user_file, "w") as f:
                f.write("")
            execute_script("login.py")
            break
        elif option == "3":
            print("Logging out...")
            execute_script("login.py")
            break
        else:
            print("Invalid option selected!")

def execute_script(script_name):
    script_path = os.path.join(os.path.dirname(os.path.realpath("__file__")), script_name)
    exec_vars = {"__file__": script_path, "__name__": "__main__"}
    with open(script_path, "rb") as f:
        exec(compile(f.read(), script_path, "exec"), exec_vars)

if __name__ == "__main__":
    main()
