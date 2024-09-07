#List [] is a collection, which is ordered and changable allows duplicate member
# *Allows duplicate value 
# *Any type data can be stored 
# *We can modify the list data type items, we can add or remove 
# insert(), append(), extend(), pop()

#CRUD
#Create
a=[1,2,3,4,5,6,7,8,9,10]
b=[10,20,30,40,50,60,70,80,90,100]

#Read
print(a)

#Update
#insert()
a.insert(0,11)
print(a[0])
print(a)
#append
a.append(110)
print(a)
#extend
a.extend(b)
print(a)

#Delete
a.pop(9)
print(a)


