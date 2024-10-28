#Class variable / static variable - both are same

class Accunt:
    min_Bal = 500
    
    @classmethod
    def get_Min_Bal(cls):
        return cls.min_Bal
    
    @classmethod
    def update_min_Bal(cls):
        cls.min_Bal = 1000
   
    
print(Accunt.get_Min_Bal())
Accunt.update_min_Bal()
print(Accunt.get_Min_Bal())