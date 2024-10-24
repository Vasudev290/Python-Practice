#Update operation
emp={}
user={'id':101,'name':'Vasu','loc':'Bangalore'}

user['name'] = 'Vasu Dev'
print(user) #{'id': 101, 'name': 'Vasu Dev', 'loc': 'Bangalore'}

user['email'] = 'vasu@gmail.com' #if it's not there in the dict element, it'll create
print(user) #{'id': 101, 'name': 'Vasu Dev', 'loc': 'Bangalore', 'email': 'vasu@gmail.com'}