#Multiplication table of a number

#For loop
table = int(input("Enter the table number :"))
for i in range(1,11):
    print(f"{table} x {i} = {table * i}")
    
#While loop
Table = int(input("Enter the table value :"))
i = 1
while i<=10:
    print(f"{Table} x {i} = {Table*i}")
    i+=1