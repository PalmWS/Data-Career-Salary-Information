# This Module has some Other Commonly used Functions

# Importing Required Modules

import os
import time


# Functions

def About():
    """
    About() -> Prints the About Information on the Terminal

    Parameters -> None
    """
    # Change the path given here to the absolute path of the README file
    with open('D:\My office\Westride\Final Project\DataCareer_Salaries\README.md') as file:
        data = file.read()
        print(data)


def ClearScreen():
    """
    ClearScreen() -> Clears the Terminal Screen

    Parameters -> None
    """

    print("Clearing..")
    time.sleep(2)
    os.system("cls")


def Menu(answer="Yes"):
    """
    Menu() -> Displays the Menu

    Parameters -> Answer (User's Choice on Displaying the Menu, by default it is set to True)
    """

    if answer in ["Yes", "Y"]:
        print("  Welcome To Data Career Salary Information")
        print("1. Apply your job")
        print("2. Cancel application")
        print("3. Show my application")
        print("4. Search Data Career information")
        print("5. Clear Screen")
        print("6. Menu")
        print("7. About")
        print("8. Exit")
    else:
        pass
