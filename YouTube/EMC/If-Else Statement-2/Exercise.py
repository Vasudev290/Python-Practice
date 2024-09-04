# 1. Get input for variable mark. if marks> 35 print pass else print fail
""" mark=int(input('Enter your Marks :'))
if(mark>35):
    print("Pass")
else:
    print("fail") """


# 2. Get input for variable income. if income is greater then 70000 schoolship is available, else not eligible for scholarship 
""" income= int(input("Income :"))
if(income > 7000):
    print("Not Eligible for scholarship")
else:
    print("Scholarship is Available") """

# 3.Get input for a number and check whether it is divisible by both 3 and 5 or not if yes then print, 
#the number is divisible by 3 and 5 else print the number is not divisible by 3 and 5 .?

""" a= int(input("Enter the Value :"))
if(a%3 == 0 and a%5 == 0):
    print("Divisible by 3 and 5")
else:
    print("Not a Divisible by 3 and 5") """

''' 4. Get input for a number and find it is even or odd'''

""" a= int(input("Enter a Value :"))
if(a%2 == 0):
    print("It's a Even Number")
else:
    print("No it's Odd Number") """

#

""" Score= int(input("Score: "))
if(Score<35):
    print("Poor Student")
elif(Score>35 and Score<70):
    print("Average Student")
else:
    print("Good Student") """


Score= int(input("Score: "))
if(Score<35):
    print("Poor Student")
elif(Score>35 and Score<70):
    print("Average Student")
elif(Score>70 and Score<100):
    print("Good Student")
else:
    print('Invaild Marks')