#Create Error message: fileExistError

fp1=open('bng.txt','x')
fp1.close()

#FileExistsError: [Errno 17] File exists: 'bng.txt'


fp=open('23oct.txt','x')
fp.write("Exclusive creation mode for write operation")
fp.close()
#If file is not created it'll create atuomatically ('x')
