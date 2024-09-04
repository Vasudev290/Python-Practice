# 1. Get input for variable mark. if marks> 35 print pass else print fail
mark=int(input('Enter your Marks :'))
if(mark>35):
    print("Pass")
else:
    print("fail") 


# 2. Get input for variable income. if income is greater then 70000 schoolship is available, else not eligible for scholarship 
income= int(input("Income :"))
if(income > 7000):
    print("Not Eligible for scholarship")
else:
    print("Scholarship is Available")

# 3.Get input for a number and check whether it is divisible by both 3 and 5 or not if yes then print, 
#the number is divisible by 3 and 5 else print the number is not divisible by 3 and 5 .?

a= int(input("Enter the Value :"))
if(a%3 == 0 and a%5 == 0):
    print("Divisible by 3 and 5")
else:
    print("Not a Divisible by 3 and 5")

''' 4. Get input for a number and find it is even or odd'''

a= int(input("Enter a Value :"))
if(a%2 == 0):
    print("It's a Even Number")
else:
    print("No it's Odd Number")

#Get input for score out of 100 
# if  score is 35 = "Poor student" 
# if score is greater then 35 but < then 70= "Average Student" 
# if score is greater then 70 = "Good student"

Score= int(input("Score: "))
if(Score<35):
    print("Poor Student")
elif(Score>35 and Score<70):
    print("Average Student")
else:
    print("Good Student")

Score= int(input("Score: "))
if(Score<35):
    print("Poor Student")
elif(Score>35 and Score<70):
    print("Average Student")
elif(Score>70 and Score<100):
    print("Good Student")
else:
    print('Invaild Marks')


# 6.Make a  mini calculator 
# Get input for 2 number a and b 
# Get input from user whether to add/sub/mul/div 
# if user selects add then the two number and print the result

a= int(input("A: "))
b= int(input("B: "))
operation= input('add/sub/mul/div :')
if(operation == 'add'):
    print(a+b)
elif(operation == 'sub'):
    print(a-b)
elif(operation == 'mul'):
    print(a*b)
elif(operation == 'div'):
    print(a/b)
else:
    print("Invalid Operation")

# 7. Get a input for score percentage. 
# only if the percentage is greater then 70, 
# get input for his name,department and location.
# then print you are eligible. if not print you are not eligible 

Score_Percentage= int(input("Your Score Percentage :"))
if(Score_Percentage >=70):
    name=input("Enter your Name :")
    age=input("Enter your age :")
    location=input("Enter your Location :")
    print("You are Eligible")
else:
    print("Not Eligible ")


# 8. If salary greater then or equal to 20000 or age less then or equal to 25, 
# get input for required loan amount. 
# If not print yo are not eligible for loan.
#if required loan amount is less then 50000 print maximum loan amount is 50000

salary=int(input("Your Salary Amount :"))
age=int(input("Enter Your Age :"))
if(salary>=20000 or age<=25):
    loan=int(input("Loan :"))
    if(loan>50000):
        print("Maximum loan amount is 50000")
    else:
        print("You are eligible for Loan")
else:
    print("Not Eligible")

# 9. Get input for five subject marks. Add of it, and find average. 
# if average mark is less then 35. 
# print "Additional class is required" 
# else print "You are good to go"

a= int(input("Telugu : "))
b= int(input("English :"))
c= int(input("Maths :"))
d= int(input("Science :"))
e= int(input("Social :"))
f=(a+b+c+d+e)/5
if(f < 35 ):
    print("Additional class is required")
else:
    print("You are good to go")