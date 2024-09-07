#Set {} is a collection, which is unordered and unchangable and unindexed, No duplicate members
# Do not allow duplicate , duplicate will be removed 
# We cannot modify the set items but we can ADD or Remove items 
# Sets are unordered 
# Add(), update(), remove(), pop()

#CRUD
#Create
a= {1,2,3,4,1,2,5,7}

#Read
print(a)

#Update
#Add()
a.add(8)

#Delete
#Remove()
a.remove(7)
#pop()
a.pop()
print(a)