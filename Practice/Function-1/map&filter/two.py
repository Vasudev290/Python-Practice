#map (function, sequnces)
#function
numbers= [10,20,30,40,50,60]

def add(numbers):
    return numbers+1

R1= map(add,numbers)
print(list(R1))

#Lambda
numbers= [10,20,30,40,50,60]
map_Obj=map(lambda numbers: numbers+1, numbers)
new_number=list(map_Obj)
print(new_number)