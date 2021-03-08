import mysql.connector
from datetime import datetime
import getpass

db = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",database = "HOTEL_MANAGEMENT")

cur = db.cursor()


def menu():
    print("-----------------------------------------------------------------------")
    print("***************************WELCOME TO HOTEL!***************************")
    return display()

def display():
    print("-----------------------------------------------------------------------")
    choice = int(input(" \n1.Booking\n2.Customer data\n3.Bill Details\n4.Logs\n5.Exit\n \nYour choice: "))
    if choice == 1:

        try:
            booking()

        except:
            print("error1")

    elif choice == 2:
        try:
            return data()

        except:
            print("error1")

    elif choice == 3:
        try:
            bill_data()
        except:
            print("error1")

    elif choice ==4:
        return get_logs()

    elif choice == 5:
        pass

def data():
    print("-----------------------------------------------------------------------")
    a = input("Press k to return to previous menu or press Enter to continue: ")
    if a =="k":
        return display()
    cid = int(input("Enter the customer ID to see their data: "))
    query = "select* from customer_data where id=('{}')".format(cid)
    cur.execute(query)
    records = cur.fetchall()
    for x in records:
        print(x)
    return data()

def bill_data():
    print("-----------------------------------------------------------------------")
    a = input("Press k to return to previous menu or press Enter to continue: ")
    if a =="k":
        return display()
    cid = int(input("Enter the customer ID to see their data: "))
    query = "select* from bill where id=('{}')".format(cid)
    cur.execute(query)
    records = cur.fetchall()
    for x in records:
        print(x)
    bill_data()

def booking():
    print("-----------------------------------------------------------------------")
    choice2 = int(input("\n1.New customer\n2.Registered customer\n3.Previous menue\n \nYour choice:  "))
    print("-----------------------------------------------------------------------")

    if choice2 == 1:
        return new_user()

    elif choice2 == 2:
        return  registered_user()


    elif choice2 == 3:
        return display()

def new_user():
    try:
        cid = int(input("Customer ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        add = input("Address: ")
        email = input("E-Mail: ")
        confirm = input(("Do you want to confirm(y/n): "))
        if confirm == "y":
            query = "insert into customer_data values ('{}','{}','{}','{}','{}')".format(cid, name, age, add, email)
            cur.execute(query)
            db.commit()

            print("Customer registered sucessfully!!")
            return booking()
        else:
            return booking()
    except:
        print("error1")

def registered_user():
    try:
        print("-----------------------------------------------------------------------")
        cid = int(input("Please enter your customer ID: "))
        bill = int(input("Enter the bill no.: "))
        cin = input("Check-in date(dd-mm-yyy):")
        out = input("Check-out date(dd-mm-yyy):")
        nom = int(input("Enter the number of days: "))
        nos = int(input("Enter the number of rooms: "))
        room = int(input("SELECT THE ROOM TYPE:\n1.Deluxe\n2.Superor\n3.Executive\nYour Choice: "))
        if room == 1:
            r1 = "Deluxe"
            t = 1000
        elif room == 2:
            r1 = "Superior"
            t = 1500
        elif room == 3:
            r1 = "Executive"
            t = 2500
        total = nos * t *nom
        print("Total Bill: ", total)
        confirm = input(("Do you want to confirm(y/n): "))
        if confirm == "y":
            query = "insert into bill values ('{}','{}','{}','{}','{}','{}','{}')".format(bill, cid, cin, out,nom, nos, r1,
                                                                                           t)
            cur.execute(query)
            db.commit()
            print("BOOKING SUCESSFULL!!")
            return display()
        else:
            return booking()

    except:
        print("error2")

def log():
    myFile = open('Log.txt', 'a')
    x = (datetime.now())
    z = ('\nAccessed by admin on '+str(x))
    myFile.write(z)

def get_logs():
    f = open("Log.txt", "r")
    print(f.read())
    return display()

log()

try:
    menu()
except:
    print("Error in menu")
