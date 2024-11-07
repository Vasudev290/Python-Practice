#Another Swap the values of two variable without using a temporary variable

a= int(input("Give a :"))  #10
b= int(input("Give b :"))  #20

a +=b    #30
b = a-b  #20
a= a-b   #10

print(f"After Swaping a Value :{a}")
print(f"After Swaping b Value :{b}")