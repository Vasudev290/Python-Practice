import re 
matcher = re.finditer("\w", "Vasu")  #small w

for match in matcher:
    print(match.start())
    
'''
0
1
2
3
'''