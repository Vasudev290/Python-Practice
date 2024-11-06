# Given string is number or not

import re
matcher = re.finditer("[0-9]", "9360390839")

for match in matcher:
    print(match.start(), match.group())
    
'''
0 9
1 3
2 6
3 0
4 3
5 9
6 0
7 8
8 3
9 9
'''