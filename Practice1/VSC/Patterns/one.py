# Print Pattrens ;
for i in range(10):
    for j in range(i):
        print("*",end= " ")
    print()


for i in range(10):
    for j in range(10-i):
        print("*",end= " ")
    print()

for i in range(10):
    for j in range(10-i):
        print(end=' ')
    for j in range(i):
        print("*",end= " ")
    print()