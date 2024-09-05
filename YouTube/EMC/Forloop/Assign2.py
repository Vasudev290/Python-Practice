#Neasted for loop
for i in range(1,6):
    for j in range(1,3):
        print(j,"Apple")


for i in range(1,3):
    print("Week :", i)
    for j in range(1,4):
        print("Day :", j) 


for i in range(1,11):
    print()
    for j in range(1, i+1):
        print(j, end=" ")


for a in range(1,11):
    print()
    for b in range(1, a+1):
        print("*", end=" ")