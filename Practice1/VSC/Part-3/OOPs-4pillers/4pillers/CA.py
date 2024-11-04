from account import Account

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
print(ca1.cal_bal())  #20000
'''
{'acc_name': 'Vasu', 'acc_email': 'Vasukesavule@gmail.com', 'acc_loc': 'Bangalore'}
{'acc_name': 'Deva', 'acc_email': 'Deva@gmail.com', 'acc_loc': 'Chennai', 'acc_id': 201, 'acc_sal': 45000}
20000
'''