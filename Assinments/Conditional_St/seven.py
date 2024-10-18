#7.Program to print given 3 numbers in ascending order?
num1= int(input("Enter the first number :"))
num2= int(input("Enter the second number :"))
num3= int(input("Enter the Third number :"))

numbers= [num1,num2,num3]

numbers.sort()

print("The numbers are ascending order :",numbers)