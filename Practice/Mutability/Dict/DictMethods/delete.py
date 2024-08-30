#pop()
emp= {
    'eid':123,
    'ename':'Arjun',
    'Sal': 45676,
    'Loc':'Bangalore',
    'Country': 'India'
}

emp.pop('eid')
print(emp)

#popitem() delete the last element for the key:value
emp.popitem()
print(emp)

#Clear()
emp.clear()
print(emp)