#Example-1
def add ():
    print('Addition')
add()
add()
'''================================='''

#Example-2
def add (a,b):
    print(a+b)
add(10,20)
add(100,200)
add(1000,2000)
#Concate
add("Hello,","Good Morning")
'''================================='''

#Example-3
#Execute some business logic
#Finally return some value
def wish(a,b,c,d):
    r1= a+b+c+d+100
    return r1
result= wish(1,2,3,100)
print(result)

