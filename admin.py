import sys
import os.path
from os import path

def main():
    select_department()
    
def select_department():
    global selected_dept, base_dir, dept_list_file
    base_dir = os.path.dirname(os.path.realpath("__file__"))
    
    dept_list_file = "alldepartments.txt"
    create_file(dept_list_file)
    
    departments = ["1. Fruit","2. Poultry","3. Meat","4. Beverage",
                  "5. Frozen Foods","6. Dietary Food","7. Kosher","8. Halal"]
    for dept in departments:
        print(dept)
    
    selected_dept = input("Select department (1-8): ")
    match_department()

def create_file(filename):
    global file_exists
    file_exists = path.exists(filename)
    if not file_exists:
        open(filename, "x").close()
    
def match_department():
    global dept_filename
    dept_map = {
        "1": "Fruit.txt", "2": "Poultry.txt", "3": "Meat.txt",
        "4": "Beverage.txt", "5": "Frozen Foods.txt",
        "6": "Dietary Food.txt", "7": "Kosher.txt", "8": "Halal.txt"
    }
    
    if selected_dept in dept_map:
        dept_filename = dept_map[selected_dept]
        verify_file()
    else:
        print("Invalid selection! Choose 1-8.")
        select_department()

def add_data(filename, content):
    with open(filename, "a") as f:
        f.write(content + ",")
        
def verify_file():
    global price_file
    create_file(dept_filename)
    price_file = "Price " + dept_filename
    create_file(price_file)
    
    if not file_exists:
        add_data(dept_list_file, selected_dept)
        
    get_product_info()

def get_product_info():
    product_count = input("How many products to add: ")
    if validate_number(product_count) != 0:
        print("Invalid input! Try again.")
        get_product_info()
    else:
        for _ in range(int(product_count)):
            get_product_name()
            get_product_price()
        next_action()

def validate_number(input_val):
    error_flag = 0
    if not input_val or input_val == "0":
        error_flag = 1
    else:
        for char in input_val:
            if not char.isdigit():
                error_flag = 1
                break
    return error_flag

def get_product_name():
    product_name = input("Enter product name: ")
    if not validate_name(product_name):
        print("Invalid name! Try again.")
        get_product_name()
    else:
        add_data(dept_filename, product_name)

def validate_name(name):
    return name.strip() != ""

def get_product_price():
    price = input("Enter product price: ")
    if validate_price(price) != 0:
        print("Invalid price! Try again.")
        get_product_price()
    else:
        add_data(price_file, price)

def validate_price(price_val):
    error_flag = 0
    decimal_count = 0
    
    if not price_val or price_val == "0":
        error_flag = 1
    else:
        for char in price_val:
            if char == ".":
                decimal_count += 1
                if decimal_count > 1:
                    error_flag = 1
                    break
            elif not char.isdigit():
                error_flag = 1
                break
    return error_flag

def next_action():
    choice = input("\n1. Select another department\n2. Log out\n3. Exit\nChoose (1-3): ")
    
    if choice == "1":
        select_department()
    elif choice == "2":
        print("Logged out successfully!")
        run_script("Login.py")
    elif choice == "3":
        print("Thank you! Goodbye!")
        sys.exit()
    else:
        print("Invalid choice!")
        next_action()

def run_script(script_name):
    script_path = os.path.join(base_dir, script_name)
    exec_params = {"__file__": script_path, "__name__": "__main__"}
    with open(script_path, "rb") as f:
        exec(compile(f.read(), script_path, "exec"), exec_params)

if __name__ == "__main__":
    main()
