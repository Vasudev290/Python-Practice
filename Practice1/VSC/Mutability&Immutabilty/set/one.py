#Set{}
"""*is a collection, which is unordered and unchangeble, unindexed. no duplicate members
*Any type of data can be stored.
*if you want to represent group of unique elements/values as one entity, nothing set
and insertion order is not preserved (no order gurantee), and no indexing concept 
**we cannot modify the set items but we can add or remove items.
*sets are unordered. 
CRUD opration
create - set(), copy()
Read - 
update - add()- Add item to set oject. 
         update()-expecting iterable object- if you want to add multiple iteams/itearable object to set.
Delete - remove(),pop(),clear(),discard()
*mutability"""

id={101,102,103,104,101,102,103,104}
ids={"id":"101"}

#no duplicate members
print(id) # {104, 101, 102, 103}
print(type(id))   #set
print(ids) #{'id': '101'}
print(type(ids))  #dict


#set
si={}
di={}
print(type(si))  #dict
print(type(di))  #dict