#Update
emp= {
    'eid':123,
    'ename':'Arjun',
    'Sal': 45676,
    'Loc':'Bangalore',
    'Country': 'India'
}

emp.update({'avail': True})
print(emp)


#SetDefault if you want set default value use set default value
emp.setdefault('Number','98765432')
print(emp)
emp.setdefault('ename','Arjun')
print(emp)