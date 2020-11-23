import mysql.connector

db = mysql.connector.connect(host = "localhost",user = "root",passwd = "root")

cur = db.cursor()


def database():
    try:
        cur.execute("CREATE DATABASE HOTEL_MANAGEMENT;")
        db.commit()
        print("Database created sucessfully!!")

    except:
        print(error)

def table1():
    try:
        cur.execute(
        "CREATE TABLE customer_data(ID int(4) Primary Key, NAME varchar(15),AGE integer, ADDRESS varchar(50), E_MAIL varchar(40))")
        cur.commit()
        print("TABLE customer_data created sucessfully!!")
    except:
        print("TABLE1 not created.")
def table2():
    try:
        cur.execute(
        "CREATE TABLE BILL(BILL_NO int(10), ID int(4) Primary Key , CHECK_IN varchar(10), CHECK_OUT varchar(10), NO_OF_ROOM INT(5), ROOM_TYPE varchar(20),TOTAL int(10))")
        cur.commit()
    except:
        print("TABLE2 not created")


choice = input(("Do you want to create the database:(y/n) "))

if choice =="y":
    database()
    choice1 = input(("Do you want to create table1 and table2:(y/n) "))
    if choice1 == "y":
        table1(), table2()













