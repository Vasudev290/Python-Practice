#Set {}
#Delete operation
# remove(),pop(),clear(),discard()
#remove - it remove specified element from  set
#discard - it remove specified element from  set

#Pop() - it removes random element from set.
name={'vasu','arjun','kumar','suresh','ankitha'}
name.pop()
print(name) #{'ankitha', 'suresh', 'vasu', 'kumar'}

#remove() - to select the particular element from the set for remove.
name1={'vasu','arjun','kumar','suresh','ankitha'}
name1.remove("kumar")
print(name1) #{'arjun', 'vasu', 'suresh', 'ankitha'}

#discard() - discard will throw error
name2={'vasu','arjun','kumar','suresh','ankitha'}
name2.discard("vasu")
print(name2) #{'ankitha', 'arjun', 'suresh', 'kumar'}

#clear() -it'll clear all the element from the set
name3={'vasu','arjun','kumar','suresh','ankitha'}
name3.clear()
print(name3) #set() empty set