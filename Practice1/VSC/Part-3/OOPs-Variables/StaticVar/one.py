#Static Variable
#If values is not varied from object to object
#Inside class, outside any method.
#Inside constr, using classname

class Account:
    min_bal = 500             #Static Method
    
    def __init__(self,id):
        self.acc_id = id
        Account.Branch_Name = 'Marathahalli'
    
    def set_bal(self):
        Account.branch_id = 421
    
    @classmethod
    def update_parent_Branch(cls):
        cls.parent_branch = "Bangalore"
        
    @staticmethod
    def tax_calc():
        Account.tax = 10
    
a1=Account(101)
print(a1.__dict__)   #{'acc_id': 101}
print(Account.__dict__)