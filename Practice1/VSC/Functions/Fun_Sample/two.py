#Another example
def add(a,b,c):
    pass


add(10,20,30)

'''
What is a,b,c : positional argument / formal arguments
what is 10,20,30: actual argument
'''

'''
Python - function arguments are 4 types
----------------------------------------
1. Positional arguments
2. keyword arguments
3. default arguments
4. variable length arguments
'''

#Positional arguments / formal arguments
#arguments that need to be included in the proper position or order. 

def sub (a,b):
    print(a-b)

sub(10,20) #-10
sub(20,10) #10

#keyword arguments
# an argument preceded by an identifier 
# (e.g. name= ) in a function call or passed as a value in a dictionary preceded by ** .

def sub (a,b):
    print(a-b)

sub(a=10,b=20) #-10
sub(b=20,a=10) #-10 

# default arguments
#values that are provided while defining functions.
def add(a,b,c):
    print(a+b+c)

add(10,20,30) #60
#add(10,20) #error

def add1(a,b,c=100):
    print(a+b+c)

add1(10,20,30) #60
add1(10,20) #130

#variable length arguments
# a way to pass a variable number of arguments to a function.
def add(*a):
    print(a)


add(10)
add(10,20)
add(10,20,30)
add(10,20,30,40)
add(10,20,30,40,50)