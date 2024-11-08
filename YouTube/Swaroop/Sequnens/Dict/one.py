#Create Dict, Access values, update values, and iterate through key-value pairs
#Method 1
""" 

My_Dict = {
    'name' : 'Vasu',
    'age' : 23,
    'city' : 'Bangalore'
} """

My_Dict = {}
name = input("Enter your Name :")
age = int(input("Enter your Age :"))
loc = input("Enter your City :")


My_Dict['name'] = name
My_Dict['age'] = age
My_Dict['loc'] = loc

My_Dict['age'] = 24
print(My_Dict) #{'name': 'vasu', 'age': 23, 'loc': 'Bangalore'}
#Access Values