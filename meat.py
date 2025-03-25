import os.path
from os import path
import sys

def main():
    Menu();

def Menu():
    global fileDir,theitem,theprice
    fileDir = os.path.dirname(os.path.realpath("__file__"));
    namesfile = open("Meat.txt","r+");
    pricesfile = open("Price Meat.txt","r+");
    items = namesfile.read().split(",");
    prices = pricesfile.read().split(",");
    length = len(items)-1;
    for i in range(length):
        print(str(i+1)+ ". " + items[i] + " - $" + prices[i]);
        
    whichone = str(input("Type a number to choose a item: "));
    CheckNum(whichone);
    if (ifcorrect != 0):
        print("Invalid, please try again");
        Menu();
    else:
        if(int(whichone) > length):
            print("Invalid, please try again");
            Menu();
        else:
            theitem = items[int(whichone)-1];
            theprice = prices[int(whichone)-1];
            Howmany();
        
def CheckNum(item):
    global ifcorrect
    ifcorrect = 0;
    numberlist = list(item)
    length = len(numberlist);
    if(length == 0 or item == "0"):
        ifcorrect = ifcorrect + 1;
    else:
        for i in range(length):
            checkitem = ord(numberlist[i])
            if(checkitem >= 48 and checkitem <= 57):
                ifcorrect = ifcorrect + 0;
            else:
                ifcorrect = ifcorrect + 1;
        
def Howmany():
    global quantity,totalprice
    quantity = str(input("How many would you like to purchas? "));
    CheckNum(quantity);
    if (ifcorrect != 0):
        print("Invalid, please try again");
        Howmany();
    else:
        totalprice = int(quantity)*float(theprice);
        msg = theitem + "," + theprice + "," + quantity + "," + str(totalprice) + ",";
        StoreInfo(msg);

def StoreInfo(message):
    adminfile = open("userinfomessage.txt","r");
    userfilename = adminfile.read();
    adminfile.close();

    adminfile2 = open(userfilename,"a");
    adminfile2.write(message);
    adminfile2.close();
    NextStep();

def NextStep():
    choice = str(input("Choose from:" +
                       "\n1. Continue in the current department" +
                       "\n2. Choose another department" +
                       "\n3. Log out" +
                       "\n4. View your receipt"+
                       "\n5. End the program"+
                       "\nEnter a number from 1 - 5:"));

    match(choice):
        case "1":
            Menu();
            
        case "2":
            filepath = fileDir + "\\Customer.py";
            
        case "3":
            print("You successfully log out!");
            filepath = fileDir + "\\Login.py";

        case "4":
            filepath = fileDir + "\\Receipt.py";
            
        case "5":
            print("Thank you, goodbye!");
            sys.exit();
            
        case default:
            print("Invalid, please enter a number from 1 - 5.");
            NextStep();
            
    filenamepath = {
        "__file__":filepath,
        "__name__":"__main__",
        };
    with open(filepath,"rb")as file:
        exec(compile(file.read(),filepath,"exec"),filenamepath);
    
    
if __name__ == "__main__":
    main();
