#Factorial of number :
num = int(input("Enter the value :"))
fact = 1
while num >0:
    fact = fact * num
    num -=1
print(fact)