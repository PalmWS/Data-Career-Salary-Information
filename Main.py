# This is the Main File that loads all the Other Modules

# Importing Required Modules

import DataSalary.User_Functions as User
import DataSalary.Other as Other
import DataSalary.Checks as Check
from time import sleep

# Initial Checks

# Checking the Connection to the MySQL Server
connection_status = Check.CheckConnection()
if connection_status is False:
    quit()
else:
    Check.CheckDatabase()  # Checking for the Requirements of the Project

# Other.ClearScreen()  # Clear the Terminal Window

# Final Imports

# Ask for the Input and Process it

Other.Menu()

while True:
    ans = input("Choose an Option Number: ")
    if ans == "1":
        User.ApplyJob()
    elif ans == "2":
        User.CancelApplication()
    elif ans == "3":
        User.ShowApplication()
    elif ans == "4":
        User.DataInfo()
    elif ans == "5":
        Other.ClearScreen()
        Other.Menu()
    elif ans == "6":
        Other.Menu()
    elif ans == "7":
        Other.ClearScreen()
        Other.About()
        while True:
            ask = input("Do you want to Display Menu(Y/N): ")
            if ask in ["Y", "y"]:
                Other.Menu()
                break
            elif ask in ["N", "n"]:
                break
            else:
                print("Please Enter either Y (Yes) or N (No)!")
    elif ans == "8":
        print("Closing all Connections..")
        sleep(0.5)
        print("Thank You!")
        quit()
    else:
        print("Please Enter a Valid Option Number!")
