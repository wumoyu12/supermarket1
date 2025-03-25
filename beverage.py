
import sys
import os.path
from os import path

def main():
    ShowMenu()

def ShowMenu():
    global fileDir, selected_item, selected_price
    fileDir = os.path.dirname(os.path.realpath("__file__"))

    user_file = open("currentuser.txt", "r+")
    currentuser = user_file.read().split(".")
    print("Welcome to the Beverage Department, " + currentuser[0] + "!")
    
    product_file = open("Beverage.txt", "r+")
    price_file = open("priceBeverage.txt", "r+")
    
    products = product_file.read().split(",")
    prices = price_file.read().split(",")
    
    for i in range(len(products)):
        print(str(i+1) + ") " + products[i] + " - $" + prices[i]);
    
    selected_number = str(input("Pick beverage by typing the number: "))
    CheckNumber(selected_number)
        
    if validation_check != 0:
        print("Invalid input, try again.")
        ShowMenu()
    else:
        if int(selected_number) > len(products)-1:
            print("Invalid number, try again.")
            ShowMenu()
        else:
            count = int(selected_number)-1
            selected_item = products[count]
            selected_price = prices[count]
            AskQuantity()

def AskQuantity():
    global quantity, totalcost
    quantity = str(input("How many would you like? "))
    CheckNumber(quantity)
    
    if validation_check != 0:
        print("Invalid input, try again!")
        AskQuantity()
    else:
        totalcost = float(quantity) * float(selected_price)
        order_message = selected_item + ","+ selected_price +","+ quantity+","+ str(totalcost) + "," 
        SaveOrder(order_message)

def SaveOrder(order_details):
    loginfile = open("currentuser.txt", "r")
    user_file_name = loginfile.read()
    loginfile.close()
    
    user_file = open(user_file_name, "a")
    user_file.write(order_details)
    user_file.close()
    
    Menu2()
    
def CheckNumber(input_item):
    global validation_check
    validation_check = 0
    num_list = list(input_item)
    
    if input_item == "" or input_item == "0":
        validation_check = 1
    else:
        for i in range(0,len(num_list)):
            ordcode = ord(num_list[i])
            if ordcode < 48 or ordcode > 57:
                validation_check = 1

def Menu2():
    menuoption = str(input("Would you like to:" +
                       "\n1) Continue shopping here" +
                       "\n2) Choose another department" +
                       "\n3) Check out" +
                       "\n4) Log Out" +
                       "\n5) Exit" +
                       "\nEnter 1-5: "))
    
    if menuoption == "1":
        ShowMenu()
    elif menuoption == "2":
        filepath = fileDir + "\\Customer.py"
    elif menuoption == "3":
        filepath = fileDir + "\\Receipt.py"
    elif menuoption == "4":
        print("Logged out successfully!")
        filepath = fileDir + "\\loginscreens.py"
    elif menuoption == "5":
        print("Thank you! Goodbye!")
        sys.exit()
    else:
        print("Invalid input, enter 1-5.")
        Menu2()
    
    filenamepath = {
        "__file__":filepath,
        "__name__":"__main__",
        };
    with open(filepath,"rb")as file:
        exec(compile(file.read(),filepath,"exec"),filenamepath);

if __name__ == "__main__":
    main()
