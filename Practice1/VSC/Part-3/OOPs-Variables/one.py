class Account:
    min_Bal = 500                   #Static Varibale
    
    def __init__(self,id,name):     #Constructor
        self.acc_id = id
        self.acc_name = name
    
    def open_Account(self):         #Instence method
        self.min_bal = 200
        
    @classmethod                    #Class method
    def get_Min_Bal(cls):
        pass
    
    @staticmethod                   #Static method
    def cal_interest():
        tax=5                       #Local variable
        
a1= Account(101,'Rahul')
a2= Account(102,'Priya')

print(a1.__dict__)  #{'acc_id': 101, 'acc_name': 'Rahul'}
print(a2.__dict__)  #{'acc_id': 102, 'acc_name': 'Priya'}