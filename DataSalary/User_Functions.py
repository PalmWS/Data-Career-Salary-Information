# This Module has the Functions that allow a User to do Certain Task's

# Importing Required Modules
import mysql.connector
import os
import datetime
import time
from mysql.connector import DataError
import random
import pandas as pd
from sqlalchemy import create_engine

# Defining Some Initial Variables
current_date = datetime.date.today()

# A Ticket can be Booked 4 Months before the Actual Trip
max_date = current_date + datetime.timedelta(days=120)


# Functions
def DataInfo():
    """
    DataInfo() -> Shows the List of Data Information according to the User Requirement

    Parameters -> None   
    """
    #setting database
    uid = 'root'
    pwd = '123456'
    host = 'localhost'
    port = 3306
    db = 'dataincome'
    con_string = f'mysql+pymysql://{uid}:{pwd}@{host}:{port}/{db}'
    con = create_engine(con_string)
    print('-------------------------------------------------')
    print("Category Information")
    print("1. Overview Jobs in Data Career")
    print("2. Interested Job")
    print("3. Expected Salary")
    print('-------------------------------------------------')
    while True:
        cat = input("Choose a category number: ")
        if cat == "1":
            csv_name = 'Overview_Jobs'
            sql = '''
                Select Job_title, avg(Salary_in_usd) as Avg_USD_Salary
                from dataincome.data_salary
                group by Job_title
                order by Avg_USD_Salary desc
            '''
            df = pd.read_sql(sql, con)
            df['Avg_USD_Salary'] = round(df['Avg_USD_Salary'], 2) #change to 2 decimal place
            pd.set_option('display.max_rows', None)
            pd.options.display.float_format = '{:,}'.format
            print(df)
            break

        elif cat == "2":
            csv_name = 'Interested_Jobs'
            Job = input('Input Job title: ')
            print('-------------------------------------------------')
            Level = input('Input Experience level \nEntry Level-"EN"\nMiddle Level-"MI"\nSenior Level-"SE"\nExpert Level-"EX"\n: ')
            print('-------------------------------------------------')
            Em_Type = input('Input Employment Type \nFull Time-"FT"\nContract-"CT"\nFreelance-"FL"\nPart Time-"PT"\n: ')
            print('-------------------------------------------------')
            sql = f'''
                Select
                    Job_title, 
                    Experience_level, 
                    Employment_type, 
                    avg(Salary_in_usd) as average_salary, 
                    min(Salary_in_usd) as min, 
                    max(Salary_in_usd) as max
                From dataincome.data_salary
                group by Job_title, Experience_level, Employment_type
                Having Job_title = '{Job}'and Experience_level = '{Level}' and Employment_type = '{Em_Type}'
            '''
            df = pd.read_sql(sql, con)
            if len(df) == 0:
                print('No data record')
            else:
                df['average_salary'] = round(df['average_salary'], 2) #change to 2 decimal place
                df['min'] = df['min'].astype(float)
                df['max'] = df['max'].astype(float)
                pd.set_option('display.max_rows', None)
                pd.options.display.float_format = '{:,}'.format
                print(df)
            break

        elif cat == "3":
            csv_name = 'Expected_salary'
            Min_Salary = input('Minimum Salary: ')
            Max_Salary = input('Maximum Salary: ')
            print('-------------------------------------------------')
            sql = f'''
                Select Job_title, Experience_level, Employment_type, Salary_in_usd, Remote_ratio, Company_location
                From dataincome.data_salary
                Where (Salary_in_usd between {Min_Salary} and {Max_Salary}) and Work_year = '2023'
                order by Salary_in_usd desc
            '''
            df = pd.read_sql(sql, con)
            if len(df) == 0:
                print('No data record')
            else:
                df['Salary_in_usd'] = df['Salary_in_usd'].astype(float)
                pd.set_option('display.max_rows', None)
                pd.options.display.float_format = '{:,}'.format
                print(df)
            break
        else:
            print('Please select correct number!')

    if len(df) != 0:
        while True:
            ask = input("Do you want to export a csv file? (Y/N): ")
            if ask in ["Y", "y"]:
                df.to_csv(f'{csv_name}.csv', index_label='id')
                print('Please wait for 3 seconds')
                time.sleep(3)
                print('Saved successfully!')
                break
            elif ask in ["N", "n"]:
                break
            else:
                print("Please Enter either Y (Yes) or N (No)!")
    else:
        pass

def ShowApplication():
    """
    ShowApplication() -> Shows the Bookings Made by an User

    Parameters -> None
    """

    mn = mysql.connector.connect(host="localhost", user="root",
                                 password="123456", database="DataIncome")
    cur = mn.cursor()

    mobile_no = input("Please Enter your 10 Digit Mobile Number: ")

    cur.execute('SELECT * FROM Job_Application where Phone="{}"'.format(mobile_no))

    result = cur.fetchall()
    if len(result) == 0:
        print("No Records Found!")
    else:
        apply_no = 1
        print(["Application_No", "Name", "Email",
                       "Phone", "Location_Country", "Job_Position", 
                       "Experience_Years","Previous_Salary"])
        for x in result:
            print("Application NO", apply_no, ":", x, "\n")
            apply_no += 1

    cur.close()
    mn.close()


def ApplyJob():
    """
    ApplyJob() -> Let's a User Book a Train

    Parameters -> None
    """

    mn = mysql.connector.connect(host="localhost", user="root",
                                 password="123456", database="DataIncome")
    cur = mn.cursor()

    #Insert Name
    while True:
        Name = input("Enter your Name: ")
        if len(Name) == 0:
            print("Please Enter a Name!")
        elif len(Name) > 255:
            print("Name too Long!")
        else:
            break

    #Insert Email
    while True:
        Email = input("Enter your Email: ")
        if len(Email) == 0:
            print("Please Enter a Email!")
        elif len(Email) > 100:
            print("Email too Long!")
        else:
            break

    #Insert Your Number
    while True:
        try:
            Mobile = input("Enter your Mobile Number: ")
        except ValueError:
            print("Please Enter a Valid Mobile Number!")
            continue
        else:
            if len(Mobile) == 10 and Mobile.isdigit() == True and Mobile != '0000000000' :
                break
            elif (len(Mobile) > 10 or len(Mobile) < 10) and Mobile.isdigit() == True:
                print("Please Enter a Valid 10 Digit Mobile Number!")
                print("Ex. '0123456789' ")
            else:
                print("Please Enter a Valid Phone Number!")
                print("Ex. '0123456789' ")

    #Insert Country
    while True:
        Country = input("Enter your living country: ")
        if len(Country) == 0:
            print("Please Enter a country")
        elif len(Country) > 50:
            print("Country name too Long!")
        else:
            break

    #Insert Job_Position
    while True:
        Job = input("Enter your job position \n(Ex. Data Analyst/Data Engineer/Sales Manager) \n: ")
        if len(Job) == 0:
            print("Please Enter a Job")
        elif len(Job) > 100:
            print("Job name too Long!")
        else:
            break

    #Insert Your Experience_Years
    while True:
        try:
            Exp = int(input("Enter your experience years: "))
            break
        except ValueError:
            print("Please Enter a experience years!")
            continue

    #Insert Your Salary
    while True:
        try:
            Salary = int(input("Enter your salary in USD: "))
        except ValueError:
            print("Please Enter salaries!")
            continue
        else:
            if Salary == 0:
                print("Please Enter correct salary!")
                print("Ex. '25000' ")
            else:
                break

    # Time_of_Application = datetime.datetime.now()
    # date = Time_of_Application.date()
    # date = date.strftime("%Y-%m-%d")

    
    # Creating Unique Application_No for each Applying
    id = random.randint(1, 10000)
    cur.execute("SELECT Application_No FROM Job_Application")
    result = cur.fetchall()
    Used_ID = []
    for x in result:
        for y in x:
            Used_ID.append(y)
    while True:
        if id in Used_ID:
            id = random.randint(1, 10000)
        else:
            break

    while True:
        ask = input("Are you Sure you want to Apply? (Y/N): ")
        if ask in ["Y", "y"]:
            print("Applying...")
            try:
                query = "INSERT INTO Job_Application values({}, '{}', '{}', '{}', '{}', '{}', {}, {}, curdate())".format(
                    id, Name, Email, Mobile, Country, Job, Exp, Salary)
                cur.execute(query)
            except DataError:
                print("Error in Applying!")
            else:
                print("Successfully Applied!")
                mn.commit()
                cur.close()
                mn.close()
                break
        elif ask in ["N", "n"]:
            print("Stopping Applying...")
            time.sleep(0.5)
            os.system("cls")
            break
        else:
            print("Please Enter Y (Yes) or N (No)!")


def CancelApplication():
    """
    CancelApplication() -> Allows a User to Cancel your application

    Parameters -> None
    """

    mn = mysql.connector.connect(host="localhost", user="root",
                                 password="123456", database="DataIncome")
    cur = mn.cursor()

    print("Please use the Show my application \n to get the Unique ID of the applying you want to Cancel!")

    while True:
        try:
            unique_id = int(input("Enter the Employee No.: "))
        except ValueError:
            print("Please Enter a Employee No.!")
        else:
            if len(str(unique_id)) == 0:
                print("Employee No.!")
            elif unique_id < 1:
                print("No. Out of Range!")
            elif unique_id > 10000:
                print("No. Out of Range!")
            elif len(str(unique_id)) != 0 and unique_id >= 1 and unique_id <= 10000:
                cur.execute(
                    "SELECT * FROM Job_Application WHERE Application_No={}".format(unique_id))
                result = cur.fetchall()
                if len(result) == 0:
                    print("No Records Found!")
                    break
                print(["Application_No", "Name", "Email",
                       "Phone", "Location_Country", "Job_Position", 
                       "Experience_Years","Previous_Salary"])
                for x in result:
                    print(x)
                while True:
                    ask = input("Are you Sure you want to Delete this(Y/N): ")
                    if ask in ["Y", "y"]:
                        cur.execute(
                            "DELETE FROM Job_Application WHERE Application_No={}".format(unique_id))
                        print("Deleted!")
                        mn.commit()
                        cur.close()
                        mn.close()
                        break
                    elif ask in ["N", "n"]:
                        break
                    else:
                        print("Please Enter either Y (Yes) or N (No)!")
                break
            else:
                print("Please Enter a Employee No.!")
