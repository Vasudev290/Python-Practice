#Constructor method
class Account:
    def __init__(self,id,name,amount): #Constructor method
        self.acc_id=id
        self.acc_name=name
        self.acc_amt=amount
        print('Inside Account class const')
        
    def open_Account(self):            #Normal Method
        print('Account opened successfully')
        
a1= Account(101,'Rahul',5000)
a1.open_Account()

a2= Account(102,'Priya',6000)
a2.open_Account()