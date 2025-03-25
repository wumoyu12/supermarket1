import os.path
from os import path
import sys

def main():
    GetUser();

def GetUser():
    global userfilename
    adminfile = open("userinfomessage.txt","r");
    userfilename = adminfile.read();
    adminfile.close();

    GetInfo();

def GetInfo():
    global infolist;
    infolist = [];
    adminfile2 = open(userfilename,"r+");
    infolist = adminfile2.read();
    adminfile2.close();
    
    DisplayInfo();

def DisplayInfo():
    displaylist = infolist.split(",");
    length = (len(displaylist)-2)/4;
    count = 1
    sum = 0;
    for i in range(0,int(length)):
        msg = "Product Name - " + displaylist[count] + ", Price - $" + displaylist[count+1] + ", Quantity - " + displaylist[count+2] + ", Total price - $" + displaylist[count+3] ;
        sum = sum + float(displaylist[count+3]);
        count = count + 4;
        print(msg);
    print("The total price of all products is $" + str(sum));
    NextStep();

def NextStep():
    fileDir = os.path.dirname(os.path.realpath("__file__"));
    choice = str(input("Choose from:" + 
                       "\n1. Choose another department" +
                       "\n2. Log out" +
                       "\n3. End the program"+
                       "\nenter a number from 1 - 3:"));

    match(choice):
        case "1":
            filepath = fileDir + "\\Customer.py";
            
        case "2":
            print("You successfully log out!");
            filepath = fileDir + "\\Login.py";
            
        case "3":
            print("Thank you, goodbye!");
            sys.exit();
            
        case default:
            print("Invalid, please enter a number from 1 - 3.");
            NextStep();

    filenamepath = {
        "__file__":filepath,
        "__name__":"__main__",
        };
    with open(filepath,"rb")as file:
        exec(compile(file.read(),filepath,"exec"),filenamepath);

if __name__ == "__main__":
    main();
