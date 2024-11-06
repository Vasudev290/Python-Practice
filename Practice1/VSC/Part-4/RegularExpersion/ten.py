#Given email is vaild gmail or not 
#vasukesavulu@gmail.com
#whitewings@info.com

import re
str = input("Enter valid Email :")
pattern = "\w[a-zA-Z0-9_.]*@gmail[.]com"
matcher = re.fullmatch(pattern,str)

if matcher!= None:
    print("Vaild Email id")
    
else:
    print("Not Valid")