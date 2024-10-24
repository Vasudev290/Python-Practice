#Update operation ;
#append(),insert(),extend(),sort(),reverse()


#append() -  list is function /method to add element to end of the list.
name=['Arjun','Aravind','Aarthi','Anshitha','Arun','Arha','Amith','Aravind','Aarthi']

name.append("Abhijith")
name.append("Anil")
print(name)
#['Arjun', 'Aravind', 'Aarthi', 'Anshitha', 'Arun', 'Arha', 'Amith', 'Aravind', 'Aarthi', 'Abhijith', 'Anil']

#insert(indexValue,"element") - we can insert element in the specified position
name1=['Arjun','Aravind','Aarthi','Anshitha','Arun','Arha','Amith','Aravind','Aarthi']
#index - 0        1          2        3          4     5       6       7        8

name1.insert(2,"AarthiVasudev")
print(name1)
#['Arjun', 'Aravind', 'AarthiVasudev', 'Aarthi', 'Anshitha', 'Arun', 'Arha', 'Amith', 'Aravind', 'Aarthi']


#extend() - Adding one more list in the list, if you given any single element it'll divide into more elements.only sequnce it'll taken
name2=['Arjun','Aravind','Aarthi','Anshitha','Arun','Arha','Amith','Aravind','Aarthi']
new_names = ['balu','bhargavi','bhanu','bala','bhagya','bhommi','bindu']
name2.extend(new_names)
print(name2)
#['Arjun', 'Aravind', 'Aarthi', 'Anshitha', 'Arun', 'Arha', 'Amith', 'Aravind', 'Aarthi', 'balu', 'bhargavi', 'bhanu', 'bala', 'bhagya', 'bhommi', 'bindu']


#Reverse() - In the list, total elements will the reverse
name3=['Arjun','Aravind','Aarthi','Anshitha','Arun','Arha','Amith','Aravind','Aarthi']
name3.reverse()
print(name3)
['Aarthi', 'Aravind', 'Amith', 'Arha', 'Arun', 'Anshitha', 'Aarthi', 'Aravind', 'Arjun']


#sort() - after the values will be default natural sorting by order.
name4=['Arjun','Aravind','Aarthi','Anshitha','Arun','Arha','Amith','Aravind','Aarthi']
name4.sort()
print(name4)
#['Aarthi', 'Aarthi', 'Amith', 'Anshitha', 'Aravind', 'Aravind', 'Arha', 'Arjun', 'Arun']

#Desending order
name5=['Arjun','Aravind','Aarthi','Anshitha','Arun','Arha','Amith','Aravind','Aarthi']
name5.sort(reverse=True)
print(name5)
#['Arun', 'Arjun', 'Arha', 'Aravind', 'Aravind', 'Anshitha', 'Amith', 'Aarthi', 'Aarthi']

#Concatination;
# one list + one list = LIST objects 
#The both values is list, we can cancate the value
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
list=l1+l2
print(list)

#Repetition 
l=[10,20,30,40,50]
li= l * 3
print(li)


#Membership operators  - in, not in
#we can check element present in list or not, 
#it'll given bool values like true or flase
member =['Arjun','Aravind','Aarthi','Anshitha','Arun','Arha','Amith','Aravind','Aarthi']
print('Arun' in member) #True
print('Arun' not in member) #false


#Identity operators - is ,is not 
#for adderss comparision
identify =['Arjun','Aravind','Aarthi','Anshitha','Arun','Arha','Amith','Aravind','Aarthi']
print("Amith" is not identify) #True
print("Amith" is identify) #false