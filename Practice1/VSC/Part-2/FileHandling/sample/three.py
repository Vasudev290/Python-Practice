fp= open('one.txt','w')

print(fp.name)
print(fp.mode)
print(fp.readable())
print(fp.writable())
print(fp.close())
fp.close()