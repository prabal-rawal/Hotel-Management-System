import mysql.connector

db = mysql.connector.connect(host = "localhost",user = "root",passwd = "root")

cur = db.cursor()


def database():
    try:
        cur.execute("CREATE DATABASE HOTEL_MANAGEMENT;")
        db.commit()
        print("Database created sucessfully!!")
        

    except:
        print("error")



database()











