#Decorater function;
#Decorator is function, it takes function as argument and return modify function 

def user_uppercase(func):

    def inner():
        msg = func()
        return msg.upper()
    
    return inner

@user_uppercase
def print_user():
    return "Hii, Rahul Gandhi"

print(print_user())