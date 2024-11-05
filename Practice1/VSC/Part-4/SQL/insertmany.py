import mysql.connector

try:
    dbcon = mysql.connector.connect(
        host="localhost", user="root", password="root", database="3pm")
    mycursor = dbcon.cursor()
    
    sql_st = '''
                insert into employee(eid,ename,esal,eloc) values (%s,%s,%s,%s)
             '''
    data =[
           (102,'Deva',56889,'New Dehli'),
           (103,'Divya',66889,'Noida'),
           (104,'Daya',76889,'Nellagiri')
           ]
        
    mycursor.executemany(sql_st,data)
    dbcon.commit()
    print("Data Inserted Successfully..!")
    
except mysql.connector.DatabaseError as err:
    if err:
        print(err)

finally:
    mycursor.close()
    dbcon.close()

