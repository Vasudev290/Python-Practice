#Polymorphism concept
#Object acting as many forms

from SA import SA
from CA import CA


def get_service(obj):
    print(obj.cal_bal())
    
    
    
get_service(SA(301,'Anil','anil@gmail.com','Chennai',65000))
get_service(CA(401,'Vijay','vijay@gmail.com','Dubai',75000))