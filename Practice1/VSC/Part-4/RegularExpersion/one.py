#Charcter classes
import re
st = input("Enter Data :")

matcher = re.finditer("[abcd]",st)

for match in matcher:
    print(match.start(),match.group())
    
    '''
    Enter Data :vasu  start()
    1
    '''
    '''
    Enter Data :vasu  match.group()
    1 a
    '''