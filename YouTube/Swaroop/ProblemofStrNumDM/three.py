#Reverse The variable
#Palidrome Concept 

s= 'palindrome'
print(s[::-1])  #emordnilap

m = 'MOM'
print(m[::-1])


palidrome = input("Enter some palidrome :")

reverse = palidrome[::-1]

if reverse == palidrome:
    print("It is a palidrome")
    
else:
    print("It is not A palidrome")