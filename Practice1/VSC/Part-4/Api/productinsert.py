import requests
import mysql.connector

dbcon = None
mycur = None

try:
    dbcon = mysql.connector.connect(host='localhost',user='root',password='root',database='11pm')
    mycur = dbcon.cursor()
    
    sql_st = '''
              insert into product(pid,pname,price,brand) 
              values (%s,%s,%s,%s,%s)
             '''
    data = []
    response = requests.get('https://dummyjson.com/products')
    product_Obj = response.json()
    
    for product in product_Obj:
        data.append((product['id'], product['title'], product['price'],product['category']))
             
    mycur.executemany(sql_st,data)
    dbcon.commit()
    print('Data inserted Successfully..!')
    
    
except mysql.connector.DatabaseError as err:
    if err:
        print(err)


finally:
    dbcon.close()
    mycur.close()