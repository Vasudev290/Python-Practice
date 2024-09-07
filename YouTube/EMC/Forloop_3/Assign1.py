# 6. Write a program to complete the sum of the first 5 natural numbers 
add=0
for i in range(1,6):
    add=add+i
print(add)

# 7. write a program to read 10 numbers from the keyboard and find their sum  and average

a=[]
print("Enter 10 Number :")
for i in range(10):
    num=int(input("Enter num :" ))
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+i
print(sum)


for i in range(1,6):
    print(i)
    for j in range(1, i+1):
        print(j, end=" ")
