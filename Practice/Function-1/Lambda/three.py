#x= lambda Argument-list: Expression

#Normal 
def update(name):
    return name.upper()

name= update('Rahul')
print(name)

#Lambda
Update =lambda name:name.lower()
name=Update('RAHUL')

print(name)
print(type(Update))