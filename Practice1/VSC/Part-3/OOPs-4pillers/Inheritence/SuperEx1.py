#Super method
#To invoke Parent class members in child class, Constructor, instenceMethod, instenceVariable, 
#syntex
#super().__init__(properties)
class Account:
    def __init__(self,name, email):
        self.acc_name = name          #Instence Variable
        self.acc_email = email        #Instence Variable
    
class SA(Account):
    def __init__(self, id, name, email, amount):
        super().__init__(name, email)
        self.acc_id = id
        self.acc_Bal = amount
        
s1=SA(101,'Vasu', 'vasu@gmail.com', 35000)
        

class CA(Account):
    def __init__(self, id, name, email, amount):
        super().__init__(name, email)
        self.acc_id = id
        self.acc_Bal = amount
        
c1=CA(102,'Deva','deva@gmail.com',40000)


print(s1.__dict__)
print(c1.__dict__)