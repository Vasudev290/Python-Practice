#set operation
s1={10,20,30,40,50}
s2={30,40,50,60,70}

#union method
print(s1)
print(s1.union(s2)) #{70, 40, 10, 50, 20, 60, 30}
print(s1 | s2) #or operation {70, 40, 10, 50, 20, 60, 30}

#difference method
print(s1-s2)  #  minus operation{10,20}
print(s1.difference(s2)) #{10,20}
print(s2.difference(s1)) #{60,70}

#intersection method
print(s1.intersection(s2)) #{40, 50, 30}
print(s1 & s2) # and operation #{40, 50, 30}

#symmetric_difference method
print(s1.symmetric_difference(s2)) #{20, 70, 10, 60}
print(s1 ^ s2) # cap{20, 70, 10, 60}