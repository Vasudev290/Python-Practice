class Account:
    min_Bal =500    #Variable
    
    
    #Methods
    def open_Acccount(self):
        print("Account opened successfully")
        
    def deposit_Account(self):
        print("Amount deposited")
        
a1=Account()

##With help of a1 we can access the class members.
print(a1.min_Bal) 
a1.open_Acccount()
a1.deposit_Account()