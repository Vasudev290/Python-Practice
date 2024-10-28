#Static Variable
#If values is not varied from object to object
#Inside class, outside any method.
#Inside constr, using classname

'''
Inside class, outside any method
inside constructor, using class name
inside instence method, using class name
inside classmethod, using cls and class name
inside static method using class name
'''
class Account:
    min_bal = 500             #Static Method
    
    def __init__(self,id):
        self.acc_id = id
        Account.Branch_Name = 'Marathahalli'
    
    def set_branchId(self):
        Account.branch_id = 421
    
    @classmethod
    def update_parent_Branch(cls):
        cls.parent_branch = "Bangalore"
        
    @staticmethod
    def tax_calc():
        Account.tax = 10
    
a1=Account(101)
a2=Account(102)

print(Account.__dict__)

a1.set_branchId()
a1.update_parent_Branch()
a1.tax_calc()

print(Account.__dict__)
