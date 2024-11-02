class Parent:
    def m1(self):
        print("Parent class - m1 method")
        
    def m2(self):
        print("Parent class - m2 method")


class child(Parent):
    def m3(self):
        print("Child class - m3 method")

'''
class child():  if You are not given anything in child class will get #AttributeError: 'child' object has no attribute 'm1'. Did you mean: 'm3'?
    def m3(self):
        print("Child class - m3 method")
'''
        
        
c1=child()
c1.m1()
c1.m2()
c1.m3()
'''
Parent class - m1 method
Parent class - m2 method
Child class - m3 method
'''