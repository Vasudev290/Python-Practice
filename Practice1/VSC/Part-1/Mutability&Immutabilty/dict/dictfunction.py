#dict functions
#get(), pop(), keys(), values(), items()

#dict.get(keys)  =return value associated with key
#pop(key)      = removes entry (key:values) from dict 
#keys() - return all keys 
#values() - return null values 
#items() - returm all key:values 
#popitem() - remove the random entry(key:value)

user={'id':101,'name':'Vasu','loc':'Bangalore'}

#get method
print(user.get('id')) #101
print(user.get('name')) #Vasu
print(user.get('loc')) #Bangalore

#pop method - it removes the specified entry in element
user.pop('id')
print(user) #{'name': 'Vasu', 'loc': 'Bangalore'}

#popitems method - it removes random entry
user.popitem()
print(user) #{'name': 'Vasu'}

emp={'id':101,'name':'Vasu','email':'vasu@gmail.com','age':23,'loc':'Bangalore'}

#Requirement - get keys(), get values(), get items()

print(emp.keys()) #dict_keys(['id', 'name', 'email', 'age', 'loc'])
print(emp.values()) #dict_values([101, 'Vasu', 'vasu@gmail.com', 23, 'Bangalore'])
print(emp.items()) #dict_items([('id', 101), ('name', 'Vasu'), ('email', 'vasu@gmail.com'), ('age', 23), ('loc', 'Bangalore')])

#type
print(type(emp.keys())) #<class 'dict_keys'>
print(type(emp.values())) #<class 'dict_values'>
print(type(emp.items())) #<class 'dict_items'>

#forloop method
for key in emp.keys():
    print(key)

for value in emp.values():
    print(value)

for k,v in emp.items():
    print(k,":",v)
