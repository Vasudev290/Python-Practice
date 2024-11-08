#Remove duplicate elements from a list to create a new list with unique element
#Method 1
lis = [10,20,30,20,40,20,50,10]
new_List = set(lis)


print(lis)  #[10, 20, 30, 20, 40, 20, 50, 10]
print(new_List) #{40, 10, 50, 20, 30}