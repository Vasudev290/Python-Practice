#File Handling 
#Read data.txt file and print content in console/terminal

fp=open('data.txt','r')   
#Type of read methods
data=fp.read()  #Whole file it'll read
data1=fp.read(10)  #No of character it'll read
data2=fp.readline()  #first line only it'll read
data3=fp.readlines()  #it'll rekad like list type it'll read
#print(data)
print(data1)
#print(data2)
#print(data3)
fp.close()