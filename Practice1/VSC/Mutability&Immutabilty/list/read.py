#Read Operation;
#index(), count(), len()

#allows duplicate members
#Len()- count the no of elements in the list.
name1=['Arjun','Aravind','Aarthi','Anshitha','Arun','Arha','Amith','Aravind','Aarthi']
print(len(name1))  #9

#Count() - Return the number of occurence.
name2=['Arjun','Aravind','Aarthi','Anshitha','Arun','Arha','Aarthi','Amith','Aravind','Aarthi']
print(name2.count('Arjun')) #1
print(name2.count('Aravind')) #2
print(name2.count('Aarthi')) #3

#Index() - for list point of view -return the index value of first occurence of specifed item
name3=['Arjun','Aravind','Aarthi','Anshitha','Arun','Arha','Aarthi','Amith','Aravind','Aarthi']
#index -  0       1         2         3        4      5       6        7        8        9     
print(name3.index('Arjun'))
print(name3.index('Aravind'))
print(name3.index('Aarthi'))
print(name3.index('Anshitha'))