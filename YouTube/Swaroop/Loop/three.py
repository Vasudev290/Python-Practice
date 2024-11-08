#print wvwn number from 1 to n

#For loop
num = int(input("Enter the number value :"))
for i in range(2,num+1,2):
    print(i)
    
    
#While loop
numb = int(input("Enter the value :"))
i = 1
while i <=numb:
    if i%2 == 0:
        print(i)
    i+=1