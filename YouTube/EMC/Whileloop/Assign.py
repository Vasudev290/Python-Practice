# 1. Print a number from 1 to 5 using while loop
i=1
while(i<6):
    print(i, end=" ")
    i=i+1

# 2. Write a loop statement to print the following series 10,20,30,.....200

i=10
while(i<=200):
    print(i, end=" ")
    i=i+10

# 3. Write a program to print first 10 natural number in reverse order
i=10
while(i>0):
    print(i, end=" ")
    i=i-1

#4. Write a program to find the factorial of a number
i=3
fact=1
while(i>0):
    fact=fact*i
    i=i-1
print(fact)