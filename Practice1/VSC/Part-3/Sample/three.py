"""
Account class created by Vasu test case 123 #Document String
"""
class Account:
    
    """Account class created by Vasu test case 123 """ #Document String
    minBal=500    #variable
    
    def open_Account(self):   #methods
        print("Account opened")
    
a1=Account()  #a1 is reference variable or object
print(a1.minBal)  #500
a1.open_Account() #Account opened

#How to print document string in console
print(Account.__doc__)#One kind of attribute,  #Account class created by Vasu test case 123