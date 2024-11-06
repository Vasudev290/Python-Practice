import requests   #first Import module
respones = requests.get('https://jsonplaceholder.typicode.com/users') #Method mention
user_Obj = respones.json()  #Convert into
print(type(user_Obj))  #<class 'list'>

#print(user_Obj)


#Print only id and name
for user in user_Obj:
    print(user['id'], user['username'],user['email'])