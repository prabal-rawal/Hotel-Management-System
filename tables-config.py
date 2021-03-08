import mysql.connector

db = mysql.connector.connect(host = "localhost",user = "root",passwd = "root",database = "HOTEL_MANAGEMENT")

cur = db.cursor()


def table():
    try:
        cur.execute("CREATE TABLE customer_data(ID int(4) Primary Key, NAME varchar(15),AGE integer, ADDRESS varchar(50), E_MAIL varchar(40))")
        bill()
    except:
        print("tables error1")
    

    
def bill():
    cur.execute("CREATE TABLE BILL(BILL_NO int(10), ID int(4) Primary Key , CHECK_IN varchar(10), CHECK_OUT varchar(10),NO_OF_DAYS int(10), NO_OF_ROOM INT(5), ROOM_TYPE varchar(20),TOTAL int(10))")
    db.commit()
    print("Tables created sucessfully")


table()

