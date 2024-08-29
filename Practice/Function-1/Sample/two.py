#Function- need to verify given number is 3 digit or not
def three_digit(num):
    if num >=100 and num<=999:
        print("Given number is 3 digit number")
    else:
        print("Not a 3 Digit number")

three_digit(23)

#Function- need to verify given number is even or not
def even_or_odd(num):
    if num %2 ==0:
        print("It's Even Number")
    else:
        print("It's Odd Number")

even_or_odd(123)