#INstence method -> set the value and get the value,

class Account:
    def set_Account_id(self,id):
        self.acc_id = id
    
    def get_Account_Id(self):
        return self.acc_id
    
    
a1 =Account()
a2 =Account()


a1.set_Account_id(101)
#print(a1.__dict__)
print(a1.get_Account_Id())
a2.set_Account_id(201)
#print(a2.__dict__)
print(a2.get_Account_Id())