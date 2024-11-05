from bank import Bank

class Account(Bank):
    
    def __init__(self,name,email,loc):             #Constructor
        self.acc_name = name
        self.acc_email = email
        self.acc_loc = loc
    
    def set_mobile_no(self,mobile):
        self.acc_mobile_no = mobile    
                                        #Encapsulation seter and getter method
    def get_mobile_no(self):
        return self.acc_mobile_no
        
    def open_account(self):
        print("Account opened successfully.!")
                                                     #instence Method
    def cal_bal(self):
        print("Account class - cal_bal method")
        
 
 #Have to use the current Account class functionlity in sa.py and ca.py
         
a1=Account('Vasu','Vasukesavule@gmail.com','Bangalore')
print(a1.__dict__)

#{'acc_name': 'Vasu', 'acc_email': 'Vasukesavule@gmail.com', 'acc_loc': 'Bangalore'}