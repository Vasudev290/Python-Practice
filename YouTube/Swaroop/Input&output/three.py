#Swap the values of two variable without using a temporary variable

a= int(input("Give a :"))  #10
b= int(input("Give b :"))  #20

temp = b
b = a
a = temp
print(f"Value of a is :", {a})
print(f"Value of b is :", {b})

'''
Give a :10
Give b :20
Value of a is : {20}
Value of b is : {10}
'''