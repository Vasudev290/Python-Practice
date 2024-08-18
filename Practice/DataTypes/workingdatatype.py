#how to represent int data type in python..!

a= 4567        #Decimal Base(0-9)
b= 0b111111    #Binary  Base (0 and 1) (0B or Ob)
c= 0o43        #Ocatal Base (0-7) (0o or 0O)
d= 0XABF       #Hexa Decial Base (0-9 and a-f or A-F)

print(a)
print(b)
print(c)
print(d)

#how to represent float data type in python..!
esal= 45000.00
print(esal)
print(type(esal))

#how to represent string data type in python..!

ename= "Arjun"
avail= "Y"
print(ename)
print(avail)
print(type(ename))
print(type(avail))

#how to represent bool data type in python..!
print(True)
print(type(True))

print(False)
print(type(False))

print(bool(0))  #False
print(bool(110)) #True

#how to represent string data type in python..!

R1= range(10000)
print(R1)
print(type(R1))

#how to represent List data type in python..!
l1 = [101,102,103,104,105,"Aravind"]  #List type Nothing but list
print(l1)
print(type(l1))

#how to represent tuple data type in python..!
t1= (10,101,1001,10001,100001,1000001, "Vasu")   #Tupletype exclty list type only
print(t1)
print(type(t1))

#how to represent set data type in python..!
s1= {101,101,102,103,103,104,105}  #Set type  unique elements/ duplicates are not allowed
print(s1)
print(type(s1))

#how to represent dict data type in python..!
d1={'id':10,'Name':'Vasu','id':10}   #Dict type  key:value pairs / duplicates are not allowed
print(d1)
print(type(d1))

#how to represent bytes data type in python..!
l1 =[101,102,103,104,255]  #bytes group of elements, range from 0 to 256 
b=bytes(l1)
ba=bytearray(l1)

'''print(l1)
print(type(l1))
print(b)
print(type(b))
print(ba)
print(type(ba))'''

print(type(l1))
print(type(b))


#how to represent bytearray data type in python..!
l1 =[101,102,103,104,255]   #bytearray group of elements, range from 0 to 256 
ba=bytearray(l1)

print(type(l1))
print(type(ba))