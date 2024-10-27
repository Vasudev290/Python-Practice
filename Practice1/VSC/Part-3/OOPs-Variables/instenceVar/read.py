#How to Read - Instence Variables
'''
Inside a class using self
Outside a class using object
'''

class Account:
    def __init__(self):             #Constructor
        self.acc_bal = 5000
    
    def get_bal(self):             #intence method
        return self.acc_bal
    
a1 = Account()
print(a1.acc_bal)    #5000
print(a1.get_bal())  #5000