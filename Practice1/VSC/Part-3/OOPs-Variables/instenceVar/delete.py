#How to Delete
'''
del self.variable name  -inside class
del object.variable name  - outide class
'''

class Account:
    def __init__(self):                   #Constructor
        self.acc_bal = 5000
    
    def get_bal(self):                    #intence variable
        return self.acc_bal
    
    def update_bal(self):                 #intence method
        self.acc_bal = 7000 
        
    def delete_bal(self):                 #intence method
        del self.acc_bal
        
        
a1 = Account()
print(a1.__dict__)   #{'acc_bal': 5000}
a1.delete_bal()  
print(a1.__dict__)   #{}

