#Super() Example
#To invoke Parent class members in child class, Constructor, instenceMethod, instenceVariable, StaticMethod
class Parent:
    def __init__(self):
        print("Parent Class - Constructor")
        
    def m1(self):
        print("Parent Class - M1 method")

class Child(Parent):
    def __init__(self):
        super().__init__()
        super().m1()
        print("Child Class - Constructor")
        
        
C1=Child()  #Child Class - Constructor