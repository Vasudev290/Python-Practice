#First Import the driver
import mysql.connector
try:
    dbcon = mysql.connector.connect(
        host="localhost", user="root", password="root", database="3pm")
    mycursor = dbcon.cursor()
    sql_Statement = '''
                    create table employee(
                        eid int,
                        ename varchar(32),
                        esal float,
                        eloc varchar(32)
                    );
                    '''
    mycursor.execute(sql_Statement)
    dbcon.commit()
    print("Table Created Successfully..!")

except mysql.connector.DatabaseError as err:
    if err:
        print(err) #We can write "unable to connect in string"

finally:
   mycursor.close()
   dbcon.close()