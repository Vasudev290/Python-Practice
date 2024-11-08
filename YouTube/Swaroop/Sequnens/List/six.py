#Count the number of occurences of a specfic elemenet in a list
#Method 1
#1,2,3,2,1,4,2,5

li = [ int(item) for item in input().split(",") ]
num = int(input())

count = 0
for i in li:
    if i==num:
        count +=1
        
print(count)
'''
1,2,3,2,1,4,2,5
2
3
'''