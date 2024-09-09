# 1. Create a class called laptop and create a following variable and functions.
# variable => processor, price, Ram
#Create object HP,DELL, LENOVA


class laptop:
    price=""
    process=""
    Ram=""

HP=laptop()
DELL=laptop()
LENOVA=laptop()

HP.price=50000
HP.process='i3'
HP.Ram='8GB'

DELL.price=75000
DELL.process='i5'
DELL.Ram='12GB'

LENOVA.price=95000
LENOVA.process='i7'
LENOVA.Ram='15GB'

print("HP Details")
print("Price :",HP.price)
print("Process :",HP.process)
print("RAM :",HP.Ram)

print("Dell Details")
print("Price :",DELL.price)
print("Process :",DELL.process)
print("RAM :",DELL.Ram)

print("LENOVA Details")
print("Price :",DELL.price)
print("Process :",DELL.process)
print("RAM :",DELL.Ram)