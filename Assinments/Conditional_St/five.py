#5.Write a program to take a single digit number from the keyboard and print in english?

num= int(input("Enter a single digit number :"))

digit_to_word={
    0:"Zero",
    1:"One",
    2:"Two",
    3:"Three",
    4:"Four",
    5:"Five",
    6:"Six",
    7:"Seven",
    8:"Eight",
    9:"Nine"
}

if 0 <= num <= 9:
    print("The number in English is :{digit_to_word[num]}")
else:
    print("Plz enter a valid single-digit number.")