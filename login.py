import sys
import os.path
from os import path

def main():
    Login();
    
def Login():
    global adminname,adminpw,fileDir
    fileDir = os.path.dirname(os.path.realpath("__file__"));
    adminname = "admin"
    adminpw = "abc123"
    global username,password
    username = str(input("Enter the username: "));
    password = str(input("Enter the password: "));
    CheckName();

def CheckName():
    if(username == "" or password == ""):
        print("Invalid input, please try again");
        Login();
    else:
        CheckAdmin();

def CheckAdmin():
    global AdminOrUser
    if(username == adminname and password == adminpw):
        print("Welcome admin!")
        AdminOrUser = "A";
    else:
        if(username == adminname):
            print("Password is incorrect")
            Login();
        else:
            CheckUser();
            AdminOrUser = "U";
    WhichOne();

def CheckUser():
    IfAdminLogin = "alldepartments.txt";
    IfExist(IfAdminLogin);
    if(TorF == "false"):
        print("Sorry, no department is ready yet because the admin never logs in...");
        choice = str(input("Please choose from the following:" +
                           "\n1. Log out" +
                           "\n2. End the program"+
                           "\nEnter a number from 1 - 2:"));
        match(choice):
            case "1":
                print("You successfully log out!");
                Login();
                
            case "2":
                print("Thank you, goodbye!");
                sys.exit();
                
            case default:
                print("Invalid, please enter a number from 1 - 2.");
                CheckUser();
    else:
        CreateUserFile();

def IfExist(thefile):
    global TorF;
    fileexist = bool(path.exists(thefile));
    if(fileexist == False):
        TorF = "false";
    else:
        TorF = "true";

def CreateUserFile():
    userfilename = username + ".txt";
    IfExist(userfilename);
    if(TorF == "false"):
        adminfile = open(userfilename,"x");
        Append(userfilename,password);
    else:
        adminfile = open(userfilename,"r+");
        fileitems = adminfile.read().split(",");
        if(fileitems[0] != password):
            print("Incorrect password/Invalid username!");
            Login();
    print("Welcome " + username + "!");
    adminfile.close();
    UserInfoMsg(); 

def Append(name,info):
    adminfile = open(name,"a");
    adminfile.write(info + ",")
    
def UserInfoMsg():
    global file
    file = "userinfomessage.txt";
    fileexist = bool(path.exists(file));
    if(fileexist == False):
        adminfile = open(file,"x");
        adminfile.close();
    Overwrite();

def Overwrite():
    adminfile = open(file,"w");
    adminfile.write(username+ ".txt");
    adminfile.close();

def WhichOne():
    if(AdminOrUser == "A"):
        filepath = fileDir + "\\Admin.py";
    else:
        filepath = fileDir + "\\Customer.py";
    
    filenamepath = {
        "__file__":filepath,
        "__name__":"__main__",
        };
    with open(filepath,"rb")as file:
        exec(compile(file.read(),filepath,"exec"),filenamepath);

        
if __name__ == "__main__":
    main();
