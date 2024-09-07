# 1. Get input for number a and b, print the number between a and b
a= int(input("Enter a Number :"))
b= int(input("Enter a Number :"))
for i in range(a+1,b):
    print(i)

# 2. Print even numbers 1 to 10
for i in range(1,11):
    if(i%2 == 0):
        print(i) 
for i in range(1,11):
    if(i%3 == 0):
        print(i)

# 3. Count the number of even number between 1 to 10
count=0
for i in range(1,11):
    if(i%2 == 0):
        count=count+1
print(count)


# 4. Count the number of odd and even numbers between 1 to 10 print it
e_count= 0
o_count=0
for i in range(1,11):
    if(i%2 == 0):
        e_count=e_count+1
    else:
        o_count=o_count+1
print(e_count)
print(o_count)

# 5. Count the number which are divisible by 3 and 5
count= 0
for i in range(1,101):
    if(i%3 == 0 and i%5 == 0):
        count=count+1
print(count)
