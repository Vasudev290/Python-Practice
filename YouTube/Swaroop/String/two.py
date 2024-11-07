#String Concatenation - you can Concatenate strings using the + #Operater

first_name = 'Vasu'
second_name = 'Dev'

full_name = first_name + " " + second_name

print(full_name)  #Vasu Dev


#String Length - you can find the length of a string using the len() function

name = 'Vasu Dev'
print(len(name)) #8


#String Methods - upper, lower, strip, replace, split, count

#Upper()
s = 'mr.chaithanya kumar'
s1 = s.upper()
print(s1)  #MR.CHAITHANYA KUMAR

#lower
s2 = s1.lower()
print(s2)  #mr.chaithanya kumar

#strip
print(s.strip()) #mr.chaithanya kumar

#replace
print(s.replace('a', 'e'))  #mr.cheithenye kumer

#split
print(s.split())  #['mr.chaithanya', 'kumar']
print(s.split(","))  #['mr.chaithanya kumar']

#count
print(s.count('a'))  #4