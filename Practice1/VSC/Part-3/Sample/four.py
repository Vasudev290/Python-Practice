"""
Class variables are three types :
--------- --------- -----------
1.instence variables -> any variable value is varied from object to object
2.Static variables -> any variable value is not varied from object to object 
                     #It's created to one copy and share it to all the members.
3.Local variables

Class methods are three types:
---------- --------- ----------
1.instence method
2.class method 
3.static method
"""
class Account:
    def open_Account(self):
        print("Account opened successfully")
        
    def deposite_Account(self,amount):
        print("Amount Deposited successfully",amount) #positional arguments



a1=Account()
a1.open_Account()
a1.deposite_Account(5000)


a2=Account()
a2.open_Account()
a2.deposite_Account(6000)