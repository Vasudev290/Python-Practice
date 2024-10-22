def division_check(func):

    def inner(a,b):
        if b==0:
            print("Can't divide by zero")
        else:
            return func(a,b)
        
    return inner

@division_check
def div(a,b):
    print(a/b)

div(10,5) #2.0
#div(10,0) #ZeroDivisionError