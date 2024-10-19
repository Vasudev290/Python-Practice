import mysql.connector

try:
    dbcon=mysql.connector.connection(host="localhost",user="root",password="root",database="dasara")
    cursor = dbcon.execute('insert into user values(102,)')
    dbcon.commit()
    print("inserted data successfully")
   
except mysql.connector.Error as err:
    print(err)
finally:
    dbcon.close()
    cursor.close()