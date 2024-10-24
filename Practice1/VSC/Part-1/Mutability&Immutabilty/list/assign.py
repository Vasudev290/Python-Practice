#Print vowels char in gienv string ?
char =input("Enter the words :")

vowels=['a','e','i','o','u']
count = 0
for word in char:
    if word in vowels:
        count = count + 1
    
print(count)