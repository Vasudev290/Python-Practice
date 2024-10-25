class Account:
    def open_Account(self):
        print("Account opened successfully")
        
    def deposite_Account(self,amount):
        print("Amount Deposited successfully",amount) #positional arguments



a1=Account(101,'Rahul') #To invoke the items we need the construtre concr is special method
a1.open_Account()
a1.deposite_Account(5000)
#TypeError: Account() takes no arguments

a2=Account(102,'Priya')
a2.open_Account()
a2.deposite_Account(6000)