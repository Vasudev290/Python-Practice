#Invoke RestAPI, Analyze data and store into mysql table.

import requests
import mysql.connector

dbcon = None
mycur = None


try:
   dbcon = mysql.connector.connect(host='localhost',user='root',password='root',database='11pm')
   mycur = dbcon.cursor()
   
   sql_st = '''
            insert into user(uid,uname,uemail,ucity,ucompany) 
            values(%s,%s,%s,%s,%s)
            '''
   data = []
   
   response = requests.get('https://jsonplaceholder.typicode.com/users')
   user_Obj = response.json()
   
   for user in user_Obj:
       data.append((user['id'], user['username'], user['email'], 
                    user['address']['city'],user['company']['name']))
   mycur.executemany(sql_st,data)
   dbcon.commit()
   print('Data Inserted Successfully..!')

except mysql.connector.DatabaseError as err:
    if err:
        print("Unable to get the user")

finally:
    dbcon.close()
    mycur.close()