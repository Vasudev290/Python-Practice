#Given mobile is indian mobile number or not
#6,7,8,9 and 10 digit number
#[6-9]\d{9}

#syntex of fullmatch
#re.fullmatch(pattren , string)

import re
Number = input('Enter mobile Number :')
match = re.fullmatch("[6-9]\d{9}", Number)

if match!=None:
    print("Given number is indian number")
    
else:
    print("Not Indian number")
    
'''
Enter mobile Number :9345632854
Given number is indian number
'''