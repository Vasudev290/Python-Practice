# Iterative sequnces
# For ele in sequnces

#Str
Ename= 'Vasu'
for ename in Ename:
    print(ename)

#List
enames= ['Arjun', 'Krishna', 'Bhimma', 'abhi']
for ename in enames:
    print(ename)

#Tuple
t= (10,20,30,40,50)
for t1 in t:
    print(t1)

#Set
set= {101,102,103,104,105}
for set1 in set:
    print(set1)

#Dict
Emp= {'id':101,'Name':"Ashavathdhama",'Age': 100}
"""for emp1 in Emp:
    print(emp1)"""
for k,v in Emp.items():
    print(k, ":", v)  