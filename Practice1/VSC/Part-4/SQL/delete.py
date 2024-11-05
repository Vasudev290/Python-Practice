import mysql.connector

try:
    dbcon = mysql.connector.connect(
        host="localhost", user="root", password="root", database="3pm")
    mycursor = dbcon.cursor()
    sql_st = ''' delete from employee where eid = 104'''
    
    mycursor.execute(sql_st)
    
    dbcon.commit()
    print("Deleted Successfully..!")
    
except mysql.connector.DatabaseError as err:
    if err:
        print("Unable to connect to database")
    
finally:
    dbcon.close()
    mycursor.close()