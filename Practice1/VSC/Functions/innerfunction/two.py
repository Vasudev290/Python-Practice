#Function variable 
'''
1.local variable : inside function only
2.global variable : entire file/module
'''
#local variable
def account():
    min_bal = 500 #Local variable - inside function only

account()
#print(min_bal) #NameError

#global variable
a=100  #Global Variable  entire file/module
def funcone():
    print(a)

def functwo():
    print(a)

def functhree():
    print(a)


funcone() #100
functwo() #100
functhree() #100


a=100          #Global Variable

def funcone():
    b=200     #Local Variable

def functwo():
    a=20
    #print(a+b)

funcone()
#functwo() #NameError



#How to convert local variable as global
def funcone():
    global a
    a=100

def functwo():
    print(a)

funcone()
functwo()