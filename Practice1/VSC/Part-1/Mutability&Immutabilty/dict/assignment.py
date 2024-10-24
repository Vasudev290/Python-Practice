employee = [{'id':101,'name':'Vasu','age':23,'email':'vasu@gmail.com','loc':'Bangalore','sal':45000},
            {'id':102,'name':'Dev','age':23,'email':'dev@gmail.com','loc':'Marthahalli','sal':55000},
            {'id':103,'name':'Anil','age':24,'email':'anil@gmail.com','loc':'Chennai','sal':65000},
            {'id':104,'name':'Vijay','age':25,'email':'vijay@gmail.com','loc':'Chennai','sal':75000},
            {'id':105,'name':'Surya','age':23,'email':'surya@gmail.com','loc':'Chennai','sal':85000},
            {'id':106,'name':'Chaithanya','age':25,'email':'chaithanya@gmail.com','loc':'Bangalore','sal':95000}
            ]

#print all employee ids
#print all employee names
#print total employee salary


#print all employee ids
for emp in employee:
    print(emp['id'])

#print all employee names
for n in employee:
    print(n['name'])


#print total employee salary
total = 0
for sa in employee:
    total = total + sa['sal']
print(total)