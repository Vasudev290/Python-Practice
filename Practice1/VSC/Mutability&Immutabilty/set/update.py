#Set{}
#Update operation

#add() - add item to set oject. 
name={'vasu','arjun','kumar','suresh','ankitha'}
name.add("Dev")
print(name) #{'vasu', 'Dev', 'ankitha', 'suresh', 'arjun', 'kumar'}

#update() -
name1={'vasu','arjun','kumar','suresh','ankitha'}
#name1.update("Dev")
print(name1) #{'arjun', 'D', 'ankitha', 'v', 'e', 'kumar', 'vasu', 'suresh'}
#if we want to upadte the group of entity element we should want to use sequense of any ojects like list,range,etc., 
name1.update(["Dev","Nandu"])
print(name1)
