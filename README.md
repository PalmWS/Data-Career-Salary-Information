Welcome to Data Career Salary Information

---------
:FOLDERS:
_________

/Dataset : Contains the data that is to be inserted in the MySQL tables in csv format
         
         Files: Data Career_salaries.csv -> Contains all the data about the data salary in the format 
                                        (Work_year, Experience_level, Employment_type, Job_title, Salary,
                                         Salary_currency, Salary_in_usd, Employee_residence, Remote_ratio, Company_location, Company_size)

/DataSalary : Contains all the files that are required by the project to work

        Files: __init__.py -> Makes the folder to be recognized as a module
               Checks.py -> This file contains the functions that verify the requirements of the Project
               InsertData.py -> This file contains the functions to insert the data in the MySQL tables
               User_Functions.py -> This file contains the function that allow a user to perform certain task
               Other.py -> This file contains some commonly used functions

-------------------
:ROOT FOLDER FILES:
___________________

Main.py -> This is the main file that connects all the other modules and is used to run the project


----------
:FEATURES:
__________

Overview: It is a Data Career Salary Information in which a user can Apply a job, cancel application,
          check Data Information etc. It uses MySQL as the backend database.

1. Apply a job: Applicants can apply for your job
2. Cancel application: Applicant can cancel the application
3. Show my application: Applicant can check their application
4. Search Data Career Information: Applicant can see the Data Career Information 
5. Clear Screen: Clears the terminal screen
6. Menu: Shows the menu
7. About: Prints the content of this file to the screen
8. Exit: Exit the program

-------------------
:ENVIRONMENT SETUP:
___________________

1. Clone the Repository to your machine.
2. Create a Virtual Environment using virtualenv or pipenv.
3. `pip3 install -r Requirements.txt` to install the required packages automatically.
4. Make sure the MySQL Service is running and change the "123456" in the files with the password and the "root" with the username of your local SQL server.
5. `python3 Main.py` to see if the program is running correctly and is able to connect to MySQL Server. (Feel free to ask for help if you face any error)

### NOTE: Step 2 is optional but highly recommended to avoid conflicting packages.
### NOTE: After Cloning the Repo rename the README.md to README.txt in order for the About() Function in /DataSalary/Other.py to work.
