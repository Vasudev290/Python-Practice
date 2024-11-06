#character classes
import re
st = input("Enter Data :")

matcher = re.finditer("[^abcd]",st)

for match in matcher:
    print(match.start(), match.group())
    
'''
Enter Data :vasu
0 v
2 s
3 u
'''