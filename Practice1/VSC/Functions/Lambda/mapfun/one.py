#Add every marks +1 in the list
marks=[35,38,49,74,63,84,42]

#for loop
new_marks=[]
for mark in marks:
    new_marks.append(mark+1)

print(marks)     #[35,38,49,74,63,84,42]
print(new_marks) #[36, 39, 50, 75, 64, 85, 43]

#Normal Function

new_marks=[]
def add_mark(mark):
    return mark+1

for mark in marks:
    new_marks.append(add_mark(mark))

print(marks)     #[35, 38, 49, 74, 63, 84, 42]
print(new_marks) #[36, 39, 50, 75, 64, 85, 43]

#What exactly Map expecting; 
#Map expecting map(1,2) 1 is function, 2 is iterable/sequnce ;
marks=[35,38,49,74,63,84,42]

def add_mark(mark):
    return mark+1

#map(1,2)
#map(function,iterable)

map_obj=map(add_mark,marks)
new_marks=list(map_obj)

print(marks)      #[35, 38, 49, 74, 63, 84, 42]
print(new_marks)  #[36, 39, 50, 75, 64, 85, 43]

#Converting into lambda function with map()
marks=[35,38,49,74,63,84,42]

#Single line lambda function
#print(list(map(lambda mark:mark+1,marks)))  #[36, 39, 50, 75, 64, 85, 43]

map_obj=map(lambda mark:mark+1,marks)
new_marks=list(map_obj)
print(marks)       #[35, 38, 49, 74, 63, 84, 42]
print(new_marks)   #[36, 39, 50, 75, 64, 85, 43]
