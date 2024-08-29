#Formal Arguments
def sub(a,b):
    print(a-b)
sub(10,20)
sub(20,10)
'''=================================='''

#Keyword Arguments
def sub(a,b):
    print(a-b)

sub(a=10,b=20)
sub(b=20,a=10)

#Positional Argumnet
def add(a,b,c):
    print(a+b+c)
add(10,20,30) #60
add(10,20) #Positional error
