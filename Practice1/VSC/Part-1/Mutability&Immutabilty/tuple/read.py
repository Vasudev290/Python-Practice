#Read opoeration;
#index(), slice()

#index()
name=('Arjun','Aravind','Aarthi','Anshitha','Arun','Arha','Amith','Aravind','Aarthi')

print(name[0])
print(name[3])
print(name[6])

#slice()
name1=('Arjun','Aravind','Aarthi','Anshitha','Arun','Arha','Amith','Aravind','Aarthi')
#index - 0        1         2          3        4      5      6         7       8
print(name1[:]) #('Arjun', 'Aravind', 'Aarthi', 'Anshitha', 'Arun', 'Arha', 'Amith', 'Aravind', 'Aarthi')
print(name1[0:4]) #('Arjun', 'Aravind', 'Aarthi', 'Anshitha')
print(name1[1:5]) #('Aravind', 'Aarthi', 'Anshitha', 'Arun')


#Sort function we can't perform
#using sorted function we can sort the function

#sorted()
name2=('Arjun','Aravind','Aarthi','Anshitha','Arun','Arha','Amith','Aravind','Aarthi')
print(tuple(sorted(name2)))
#('Aarthi', 'Aarthi', 'Amith', 'Anshitha', 'Aravind', 'Aravind', 'Arha', 'Arjun', 'Arun')

number=(426,938,2,9,63,94,41,3,43,98)
result=sorted(number)
print(result) #but it'll converted into list function [2, 3, 9, 41, 43, 63, 94, 98, 426, 938]
print(tuple(result)) #(2, 3, 9, 41, 43, 63, 94, 98, 426, 938)
