a=100 #Global variable

def funct1():
    b=200 #Local variable, scope is with in the function

def func2():
    a=20
   # print(a+b) #error

funct1()
func2()