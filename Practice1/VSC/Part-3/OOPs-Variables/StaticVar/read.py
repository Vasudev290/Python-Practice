#How to Read
'''
inside a constructor -using classname,self variable
inside instence method -using classname,self
inside classmethod -cls, classname
inside static method - using classname
outside a class - using class, object
'''

class Test:
    
    a=100  #Static variable; only one copy is going to create, and share it to all the members
    
    def m1(self):      #instence method
        print(Test.a)
        print(self.a)
        
    @classmethod       #classmethod
    def m2(cls):
        print(Test.a)
        print(cls.a)
        
    
t1= Test()

""" print(Test.a)  #100
print(t1.a)   #100 """

t1.m1()
t1.m2()