# 1.Create a function called add(), sub(), multi() and div()
#Add
def add():
    print("Addition")
    a=int(input("Enter the A value: "))
    b=int(input("Enter the B value: "))
    print(a+b)

add()

#Sub
def sub():
    print("Subtraction")
    a=int(input("Enter the A value: "))
    b=int(input("Enter the B value: "))
    print(a-b)

sub()

#Multi
def multi():
    print("Multiple")
    a=int(input("Enter the A value: "))
    b=int(input("Enter the B value: "))
    print(a*b)

multi()

#Division
def div():
    print("Division")
    a=int(input("Enter the A value: "))
    b=int(input("Enter the B value: "))
    print(a/b)

div()

def painter(msg):
    print("Message :",msg)

painter("Paint my House..!")

# 2. Get a integer number from user add pass it to the function called findevenrodd().let the function print whether the number is even or odd

def findevenrodd(b):
    if(b%2==0):
        print("Even Number")
    else:
        print("Odd Number")
a=int(input("Enter A value :"))     
findevenrodd(a)

# 3. Get a integer number from user add pass it to the function called findpassorfail().let the function print whether the number is even or odd

def findpassorfail(c):
    if(c%3==0):
        print("It's a Odd number")
    else:
        print("It's not odd number")
d=int(input("Enter the Odd Number :"))
findpassorfail(d)
   
# 4. Get input for a and b and pass it to the function called printrange() let the function print number from a to b.

def printrange(r1,r2):
    for i in range(r1,r2):
        print(i)
a= int(input("Enter a :"))
b= int(input("Enter b :"))
printrange(a,b)
