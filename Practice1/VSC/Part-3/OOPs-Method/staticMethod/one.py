#Static Method
#To ceate general utility methods,we are going to use static methods(+,-,*,/)
#there's no special arguments(cls,self)

class Account:
    
    @staticmethod
    def cal_tax(p,r,t):
        return p*r*t/100
    
print(Account.cal_tax(100000,2,1)) #2000.0