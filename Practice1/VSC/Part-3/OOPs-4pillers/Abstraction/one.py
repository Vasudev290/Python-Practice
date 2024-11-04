#Hiding essential details
from abc import *
class Account:
    
    def __init__(self):    #Constructor
        pass
    
    def m1(self):          #Instence Method
        pass
    
    @classmethod           #Class Method
    def m2(cls):
        pass
    
    @staticmethod          #Static Method
    def m3():
        pass
    
    @abstractmethod     #To Achive abstract method will use abstract method #AbstractMethod
    def m4(self):
        pass
    
    
print(Account().m1())