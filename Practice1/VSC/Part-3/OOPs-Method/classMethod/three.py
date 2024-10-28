class Account:
    No_of_object = 0
    
    def __init__(self):
        Account.No_of_object = Account.No_of_object + 1
    
    @classmethod    
    def get_noofobjects(cls):   #cls is spl variable to access the static variable
        return cls.No_of_object




a1 =Account()
a2 =Account()
a3 =Account()
a4 =Account()

print(Account.No_of_object)  #4
print(Account.get_noofobjects()) #4