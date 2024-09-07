#Neasted for loop
for i in range(1,6):
    for j in range(1,3):
        print(j,"Apple")


for i in range(1,3):
    print("Week :", i)
    for j in range(1,4):
        print("Day :", j) 

#Number Order
for i in range(1,11):
    print()
    for j in range(1, i+1):
        print(j, end=" ")

#Normal "*" order
for a in range(1,11):
    print()
    for b in range(1, a+1):
        print("*", end=" ")

#Normal "#" Order
for c in range(1,6):
    print()
    for d in range(1, c+1):
        print("#",end=" ")


#Reverse Order
for r in range(6, 0, -1):
    for c in range(r):
        print("*", end=" ")
    print()