# This Module has the Functions that Verify the Requirements of the Project

# Importing Required Modules

import mysql.connector as con
from mysql.connector.errors import ProgrammingError, Error
import DataSalary.InsertData as Insert

# Functions


def CheckDatabase():
    """
    CheckDatabase() -> Checks if the Database required Exists or not

    Parameters -> None
    """

    print("Checking Database Requirements..")

    db = con.connect(host="localhost", user="root",
                     database="", password="123456")
    cur = db.cursor()
    result = None

    try:
        cur.execute("use DataIncome;")
    except ProgrammingError:
        print("Database does not Exist!")
        result = False
    else:
        result = True

    if result is True:
        print("Database exists!")
    else:
        print("Creating Database with the Required Tables..")
        print("Please be Patient!")
        cur.execute("create database DataIncome;")
        cur.execute("use DataIncome;")
        CreateTables()
        print("Database and Tables Created!")

    cur.close()
    db.close()


def CreateTables():
    """
    CreateTables() -> Creates all the Required Tables

    Parameters -> None
    """

    db = con.connect(host="localhost", user="root",
                     database="DataIncome", password="123456")
    cur = db.cursor()

    cur.execute(
        "create table Data_Salary (Work_year INT NOT NULL, Experience_level varchar(10) NOT NULL, Employment_type varchar(10) NOT NULL, Job_title varchar(100) NOT NULL, Salary INT NOT NULL, Salary_currency varchar(10) NOT NULL, Salary_in_usd INT NOT NULL, Employee_residence varchar(10) NOT NULL, Remote_ratio INT NOT NULL, Company_location varchar(10) NOT NULL, Company_size varchar(10) NOT NULL);")

    cur.execute("create table Job_Application (Application_No INT NOT NULL, Name varchar(255) NOT NULL, Email varchar(100) NOT NULL, Phone varchar(20) NOT NULL, Location_Country varchar(50) NOT NULL, Job_Position varchar(100) NOT NULL, Experience_Years INT NOT NULL, Previous_Salary_in_usd INT NOT NULL, Date_Of_Application Date NOT NULL);")

    Insert.InsertDataSalary()

    cur.close()
    db.close()


def CheckConnection():
    """
    CheckConnection() -> Tests the Connection with the Mysql Server

    Parameter -> None
    """

    try:
        print("Checking the Connection to the MySQL Server..")
        connection = con.connect(host='localhost',
                                 database='',
                                 user="root",
                                 password="123456")
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server Version", db_Info)

    except Error:

        print("Error connecting to MySQL Server, Make sure the MySQL Server is running and then try again!")
        print("Exiting!")
        return False

    else:
        return True
