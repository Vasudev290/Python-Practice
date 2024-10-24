#Read no of the emp and data from user, point in emp.csv

import csv 
fp=open('emp.csv','w',newline="")
csv_obj=csv.writer(fp)

csv_obj.writerow(["Emp_id",'Emp_Name','Emp_Sal','Emp_Loc'])

num=int(input("Enter the num of Employee :"))

for i in range(num):
    Emp_id = input("Enter Eid :")
    Emp_Name = input("Enter Ename :")
    Emp_Sal = input("Enter Esal :")
    Emp_Loc = input("Enter Eloc :")

    csv_obj.writerow([Emp_id,Emp_Name,Emp_Sal,Emp_Loc])
    print("Data Inserted Successfully!")
fp.close()