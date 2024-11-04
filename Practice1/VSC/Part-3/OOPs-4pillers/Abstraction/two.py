from abc import *
class Account:                 #Parent Class in inheritence
    
    @abstractmethod
    def cal_bal(self):
        pass
    
    
class SA(Account):             #Child Class in inheritence
    pass 