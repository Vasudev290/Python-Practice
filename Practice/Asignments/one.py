# 1.Program to check if a number is divisible by 7 or not?

num= int(input("Enter  the value :"))
if(num%7 == 0):
    print("Divisible by 7")
else:
    print("Not Divisible by 7")    

# 2. Program to check if a number is multiple of 3 not not?

number=int(input("Enter the value :"))
if(number%3 == 0):
    print("Divisible by 3")
else:
    print("Not Divisible by 3")

# 3. Program to check if a number is a 3-digit number or not?

Number=int(input("Enter the 3 digit value :"))
if(100 <= abs(Number) <= 999):
    print("Yeah it's 3digits number")
else:
    print("Sorry bro it's not a 3digit number")