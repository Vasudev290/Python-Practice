#Tuple () is a collection which is ordered and uunchangable allows duplicate members.
# *Allows duplicate value 
# *Any type of data we can store 
# *We cannot modify the tuple items 
# *We cannot add or remove
# *We can only create and Read we can't update and delete
#Create
a=(1,2,3,4,5,6,7,8,9,10)
#Read
print(a)

b=list(a)
#update 
#insert()
b.insert(0,11)
#append()
b.append(111)
#extend()
c=[111,222,333,444,555,666]
#b.extend(c)
#Delete
b.pop(5)
print(b)