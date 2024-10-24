#delete operation
emp={}
user={'id':101,'name':'Vasu','loc':'Bangalore'}

#delete method - we are deleteing complete dict object
del user['id'] #use del key word
print(user) #{'name': 'Vasu', 'loc': 'Bangalore'}

#clear()
user.clear()
print(user) #empty {}

