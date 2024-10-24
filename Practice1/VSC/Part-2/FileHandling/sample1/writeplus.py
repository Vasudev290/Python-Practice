#W+ Mode
#w+ Write and read mode, but this we'll be overwrite

st= "Hello, Good morning !"

fp=open('Statement.txt','w+')
fp.write(st)

data=fp.read()
print(data)

fp.close()