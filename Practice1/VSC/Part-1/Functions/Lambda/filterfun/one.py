#Filter_function
'''
map() - map(function,Sequnece)
filter() -filter(function,Sequnece)
reducer() - (function,Sequnece)- functiontools
'''

numbers=[1,2,3,4,5,6,7,8,9,10]
odd_num=[]
for num in numbers:
    if num %2!= 0:
        odd_num.append(num)

print(numbers) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(odd_num) #[1, 3, 5, 7, 9]


#With Function and filter method:
def is_odd(number):
    if number%2!= 0:
        return True
    else:
        return False
    
new_odd=list(filter(is_odd,numbers))
print(numbers)  #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(new_odd)  #[1, 3, 5, 7, 9]


#with lambda function and filter method;
filter_obj=filter(lambda number:number%2!= 0,numbers)
new_odd_number=list(filter_obj)

print(numbers)         #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(new_odd_number)  #[1, 3, 5, 7, 9]