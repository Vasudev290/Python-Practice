#special character
import re
matcher = re.finditer("[\s]", "rahul gandhi Bangalore") #given string space is there or not
#                              0123456789101112
#                                   5       12
for match in matcher:
    print(match.start(),match.group())