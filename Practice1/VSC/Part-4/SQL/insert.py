import mysql.connector

try:
    dbcon = mysql.connector.connect(
        host="localhost", user="root", password="root", database="3pm")
    mycursor = dbcon.cursor()
    
    sql_st = '''
         insert into employee values(101,'Vasu',35000.00,'Bangalore'),(102,'Deva',45000.00,'Chennai');
        '''
        
    mycursor.execute(sql_st)
    dbcon.commit()
    print("Data Inserted Successfully..!")
    
except mysql.connector.DatabaseError as err:
    if err:
        print(err)

finally:
    mycursor.close()
    dbcon.close()

