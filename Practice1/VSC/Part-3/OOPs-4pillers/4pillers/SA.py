from account import Account

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

'''
{'acc_name': 'Vasu', 'acc_email': 'Vasukesavule@gmail.com', 'acc_loc': 'Bangalore'}
{'acc_name': 'Vasu', 'acc_email': 'Vasukesavulu@gmail.com', 'acc_loc': 'Bangalore', 'acc_id': 101, 'acc_sal': 35000}
30000
'''

'''
{'acc_name': 'Vasu', 'acc_email': 'Vasukesavulu@gmail.com', 'acc_loc': 'Bangalore', 
'acc_id': 101, 'acc_bal': 35000, 'acc_mobile_no': 9360390839}
'''