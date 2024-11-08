#Count the number of occurences of a specfic elemenet in a list
#Method 2
#1,2,3,2,1,4,2,5

li = [ int(item) for item in input().split(",") ]
num = int(input())

count = li.count(num)
print(count)

'''
1,2,3,2,1,4,2,5
1
2
'''