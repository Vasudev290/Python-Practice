#Readplus mode 
#r+ : read and write data into file
#It can't overwrite,
#after createing in the data in read mode, then attching write data into the write mode
#file has data is there, data in the file, will not be deleted

fp=open('data.txt','r+')

data=fp.read()
fp.write("Hello, Good Morning")
print(data)

fp.close()