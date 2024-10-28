#Local variable
class Test:
    a=100            #Static Variable
    
    def m1(self):    #instence variable
        self.b=200
        c=300        #Local variable instence only we can use the local variable(Scopes is with the function)
        print(c)
        
    def m2(self):
        pass
        #print(c)   #NameError

t1= Test()
t1.m1()
t1.m2()