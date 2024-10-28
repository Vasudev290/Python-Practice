class Account:
    No_of_object = 0
    
    def __init__(self):
        Account.No_of_object = Account.No_of_object + 1




a1 =Account()
a2 =Account()
a3 =Account()
a4 =Account()

print(Account.No_of_object)  #4