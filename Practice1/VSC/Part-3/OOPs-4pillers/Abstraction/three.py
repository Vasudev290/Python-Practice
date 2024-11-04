#Sample Example of Abstractmethod

#Bank.py
from abc import *         #How to convert abstract class?
class Bank(ABC):               #Any class extending ABC class, class constains atleast one abstract- We called as abstract class
    @abstractmethod       #for object classes, we can't create object.
    def cal_bal(self):    #child class - responsible to provide the implementation.
        pass
    
#Account.py
class Account:
    def cal_bal(self):
        pass
    
#SA.py                         object acting as many forms only;

#from account import Account

class SA(Account):
    min_bal = 5000        #Static variable
    def __init__(self, id, name, email, loc, amount):
        super().__init__(name, email, loc)
        self.acc_id = id
        self.acc_bal = amount
        
    def cal_bal(self):
        return self.acc_bal - self.min_bal   #30000



sa1 = SA(101,'Vasu', 'Vasukesavulu@gmail.com','Bangalore',35000)
print(sa1.__dict__)
print(sa1.cal_bal())

sa1.set_mobile_no(9360390839)
print(sa1.get_mobile_no())   #9360390839        #Encapsulation
print(sa1.__dict__)

#CA.py

#from account import Account

class CA(Account):
    min_bal = 25000         #Static Variable
    def __init__(self, id, name, email, loc, amount):
        super().__init__(name, email, loc)
        self.acc_id = id
        self.acc_bal = amount
        
    def cal_bal(self):
        return self.acc_bal - self.min_bal
        
        
        
ca1 = CA(201,'Deva', 'Deva@gmail.com', 'Chennai', 45000)
print(ca1.__dict__)
print(ca1.cal_bal())