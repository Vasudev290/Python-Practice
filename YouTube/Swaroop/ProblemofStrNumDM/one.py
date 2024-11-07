#Vowel Counter (A, E, I, O, U)
#Write a program to calculate string inputs 

s = input("Give some words :")
s1 = s.lower()

a = s1.count('a')
e = s1.count('e')
i = s1.count('i')
o = s1.count('o')
u = s1.count('u')

print(f"Number of Vowels : {a+e+i+o+u}")

'''
Give some words :Elephant
Number of Vowels : 3
'''

