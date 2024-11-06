import re 
matcher = re.finditer("\W", "V@su")  #capital w

for match in matcher:
    print(match.start())
    
'''
 1 @
'''