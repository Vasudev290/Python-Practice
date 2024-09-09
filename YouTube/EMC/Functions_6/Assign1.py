# 5. Set s_username='VASU' s_password='123' Get input for uname and password create a function called validate. 
# if uname and password matches the function should return true else false.

s_username="vasu"
s_password="123"

uname=input("Enter username :")
password=input("Enter Password :")
def validate():
    if(s_username==uname and s_password==password):
        return True
    else:
        return False
       
a=validate()
print(a) 


# 6. (a+b)*c 
# Get input for a and b and function called add() 
# which should return the sum of a and b and multiply that sum with c

def plus(a1,a2):
    return a1+a2

a=int(input("Enter a value :"))
b=int(input("Enter b value :"))
c=int(input("Enter c value :"))

added=plus(a,b)
mulitply=added*c

print(mulitply)