# 8.Program to print given 3 numbers in descending order

num1=int(input("Enter the first value :"))
num2=int(input("Enter the second value :"))
num3=int(input("Enter the Third value :"))

number=[num1,num2,num3]

number.sort(reverse=True)

print("The numbers are ascending order :",number)