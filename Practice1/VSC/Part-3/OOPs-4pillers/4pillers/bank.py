#4pillers concept
from abc import *  #abc, abstractmethod

class Bank(ABC):
    
    @abstractmethod
    def cal_bal(self):
        pass
    
    