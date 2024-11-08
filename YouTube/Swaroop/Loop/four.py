#print odd number from 1 to num

#for loop
num = int(input("Enter the value :"))
for i in range(1,num+1,2):
    print(i)
    
#while loop
numb = int(input("Enter the value :"))
i = 1
while i<=numb:
    if i%2 != 0:
        print(i)
    i+=1