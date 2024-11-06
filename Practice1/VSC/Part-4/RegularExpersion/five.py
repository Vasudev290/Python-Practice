#chartacter classes
# Given string is number or not

import re
matcher = re.finditer("[^0-9]", "91+9360390839")

for match in matcher:
    print(match.start(), match.group())
    
'''
2 + (91 +)
'''