import sys
import os.path
from os import path

def main():
    customer_shopping()

def customer_shopping():
    base_dir = os.path.dirname(os.path.realpath("__file__"))
    
    with open("alldepartments.txt", "r") as f:
        available_depts = [int(num) for num in f.read().split(",") if num]
    
    department_names = ["Fruit", "Poultry", "Meat", "Beverage", 
                       "Frozenfood", "Dietfood", "Kosher", "Halal"]
    
    while True:
        print("\n=== MAIN MENU ===")
        print("Available Departments:")
        for idx, dept_num in enumerate(available_depts, 1):
            print(f"{idx}. {department_names[dept_num-1]}")
        
        print("\n9. View Cart")
        print("0. Logout")
        
        choice = input("\nSelect department or option (1-9, 0): ")
        
        if choice == "0":
            print("Logging out...")
            execute_script("login.py")
            break
        elif choice == "9":
            execute_script("receipt.py")
            break
        elif choice.isdigit() and 1 <= int(choice) <= len(available_depts):
            selected_dept = department_names[available_depts[int(choice)-1]-1]
            execute_script(f"{selected_dept.lower()}.py")
        else:
            print("Invalid selection! Please try again.")

def execute_script(script_name):
    script_path = os.path.join(os.path.dirname(os.path.realpath("__file__")), script_name)
    exec_vars = {"__file__": script_path, "__name__": "__main__"}
    with open(script_path, "rb") as f:
        exec(compile(f.read(), script_path, "exec"), exec_vars)

if __name__ == "__main__":
    main()
