#How to Update 
'''
Inside a class - using self
outside a class - using object 
'''


class Account:
    def __init__(self):              #Constructor
        self.acc_bal = 5000
    
    def get_bal(self):               #intence method
        return self.acc_bal
    
    def update_bal(self):            #intence method
        self.acc_bal = 7000
    
a1 = Account()
print(a1.acc_bal)    #5000
print(a1.get_bal())  #5000

a1.update_bal()
#print(a1.update_bal())

print(a1.acc_bal)    #7000
print(a1.get_bal())  #7000