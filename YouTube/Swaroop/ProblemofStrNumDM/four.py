#Find the largest three number 
a = input()

x,y,z = a.split(",")
num1 = int(x)  #10
num2 = int(y)  #20
num3 = int(z)  #30 

great = 0
if num1 > num2 :
    if num1 > num3:
        great = num1
    else:
        great = num3

elif num2 > num1:
    if num2 >num3:
        great = num2
    else:
        great = num3
        
elif num3 > num1:
    if num3 > num2:
        great = num3
    else:
        great = num2
        
print(great)