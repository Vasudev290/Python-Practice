#sample of function;

def add():
    print('Addition')

add() #Addition
add() #Addition
add() #Addition



def add(a,b): #passing argument as paremeter
    print(a+b)

add(10,20) #30 argument
add(100,200) #300 argument
add('Hello','Gm') #HelloGm argument #concatenation


#Function can perform end no of times;
def wish(a,b,c,d): # execute some business logic #finally return some value
     r1=a+b+c+d+100
     return r1


result = wish(1,2,3,4)
print(result) #110

#function - need to verify given number is 3 digit number or not

def three_digit(num):
    if num >= 100 and num <= 999:
        print("Given number is 3 digit number")
    else:
        print("Not a three digit number")

three_digit(1000)

#function - need to verify given number is even number or odd number

def even_or_odd(number):
    if number % 2 == 0:
        print("Yeah! it's even number")
    else:
        print("No it's odd number")

even_or_odd(20)