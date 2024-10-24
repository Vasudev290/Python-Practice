#Choise function => It won't genarate any random numbers but, it will return random element from the list,tuple,set and Sequence
from random import choice

enames=['Vinay','vijay','Vasu','Varun','Veeru']
        

for i in range(20):
    print(choice(enames))
'''
Varun
Varun
Vinay
vijay
Vinay
Vasu
Vinay
Vinay
Veeru
Veeru
Veeru
Vasu
Veeru
vijay
Varun
Veeru
Vasu
Varun
vijay
Vinay
'''