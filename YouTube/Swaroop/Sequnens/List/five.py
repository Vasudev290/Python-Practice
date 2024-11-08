#Remove duplicate elements from a list to create a new list with unique element
#Method 3
#10,20,30,20,40,20,50,10

inp = input().split(",")

li = [int(item) for item in inp]
s = set(li)
new_li = list(s)

print(new_li)
'''
10,20,30,20,40,20,50,10
[40, 10, 50, 20, 30]
'''