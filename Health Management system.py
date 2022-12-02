"""This is a program for Health management system
There are three clients A,B and C
We need user(dietician) to select a client
Then select what data he needs to enter for the client - Exercise or Diet
Then enter data which will be written to a file. There will be 2 files each for a client - one file for Diet and other for Exercise
Also, make sure to insert current time while entering this data
Also, write a function to retrieve this data"""

import datetime
T = str(datetime.datetime.now())

def retrieve_data(y,z):

    F_name = y+"-"+z1
    F1 = open(F_name)
    return print(F1.read())

def enter_data(j,k):
    f_name1 = j+"-"+z2
    print(f_name1)
    try:
        file = open(f_name1, "x")
        print("Please enter data:")
        user_input = input()
        file = open(f_name1, "a")
        file.write(user_input)
        file.write(" ")
        file.write(T)
        file.close()
    except:
        print("Please enter data:")
        user_input = input()
        file = open(f_name1, "a")
        file.write(user_input)
        file.write(" ")
        file.write(T)
        file.close()


while True:
    a = int(input("Select 1 to retrieve data and 2 to enter data or 0 to exit the program"))
    if a == 1:
        y = input("Name of client") #User enters A or B or C
        z = int(input("Press 1 for Exercise and 2 for diet"))
        z1 = ""
        if z == 1:
            z1 = "Exercise"
        else:
            z1 = "Diet"
        retrieve_data(y,z)
    elif a == 2:
        j = input("Name of client") #User enters A or B or C
        k = int(input("Press 1 for Exercise and 2 for diet"))
        z2 = ""
        if k == 1:
            z2 = "Exercise"
        else:
            z2 = "Diet"
        enter_data(j,k)
    elif a == 0:
        break