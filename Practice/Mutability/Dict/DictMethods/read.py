emp= {
    'eid':123,
    'ename':'Arjun',
    'Sal': 45676,
    'Loc':'Bangalore',
    'Country': 'India'
}

print(emp['eid'])
#Using get method
print(emp.get('eid'))

#Reading Method
#Key()
for key in emp.keys():
    print(key)

#Value()
for value in emp.values():
    print(value)

#Items()
for k,v in emp.items():
    print(k,':',v)


