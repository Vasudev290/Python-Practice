#Remove duplicate elements from a list to create a new list with unique element
#Method 2
#10,20,30,20,40,20,50,10

inp = input().split(",")

li = [int(item) for item in inp]

#Remove duplicate and create a new list

newL = []

#iterate over all the elements

for i in li:
    if i in newL:
        continue
    else:
        newL.append(i)
print(newL)

""" 10,20,30,20,40,20,50,10
[10, 20, 30, 40, 50] """