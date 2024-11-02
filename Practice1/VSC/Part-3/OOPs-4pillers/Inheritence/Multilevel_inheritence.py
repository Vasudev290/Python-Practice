#MultiLevel Inheritence 
class GrandParents:
    def m1(self):
        print("GrandParent class - m1 Method")
    
class Parent(GrandParents):
    def m2(self):
        print("Parent class - m2 Method")
    
class child(Parent):
    def m3(self):
        print("Child class - m3 Method")
    
c1=child()
c1.m1()
c1.m2()
c1.m3()