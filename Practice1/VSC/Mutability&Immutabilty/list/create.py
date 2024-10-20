#list=[]
#Group of element as one entity,where allowed duplicates and hetrogenious.
#List CRUD
#Create
l1=[]
l2=[10,20,30,40,50,60,70,80] # or l1=list(range(10)) or l2=eval(input("Enter the list :"))
#l3=eval(input("Enter list :"))
l4=list(range(10))
l5= "Vasu Dev".split()
print(l1)
print(l2)
#print(l3)
print(l4)
print(l5)

#Read 
""" ids=[101,202,303,404,505,606,707,808]
name=['vasu','arjun','kumar','suresh']
print(ids)
print(name) """

#Indexing Concept
""" ids=[101,202,303,404,505,606,707,808]
name=['vasu','arjun','kumar','suresh']
#print(ids[indexing no:0])

print(ids[0])
print(ids[1])
print(ids[2])
print(ids[3])
print(name[0])
print(name[1])
print(name[2])
print(name[3]) """

#For loop method
ids=[101,202,303,404,505,606,707,808,98]
name=['vasu','arjun','kumar','suresh','ankitha']

for id in ids:
    print(id)

for n in name:
    print(n)

#Whileloop method
#ids
i=0
while i<=8:
    print(ids[i])
    i=i+1
#names
i=0
while i<=4:
    print(name[i]) 
    i=i+1
