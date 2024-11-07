''' Calculate Program
input :
num1
num2
operation

output:
perform the operation on the inputs

'''

num1 = int(input("Enter the 1st Number :"))
num2 = int(input("Enter the 2st Number :"))

operation = input("Given the operator : ")

if operation == '+':
    print(f"Addition ➕ of 2 Value is :{num1 + num2}")
    
elif operation == '-':
    print(f"Subtraction ➖ of 2 value is :{num1 - num2}")
    
elif operation == '*':
    print(f"Multiple ✖️ of 2 value is : {num1 * num2}")
    
elif operation == '/':
    print(f"Division ➗ of 2 value is :{num1 / num2}")
    
else: 
    print("Not Valid Operator..!😣")