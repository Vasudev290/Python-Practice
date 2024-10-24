#Decorater function;
#Decorator is function, it takes function as argument and return modify function 

def outer1():
    print("Outer function")

    def inner():
        print("Inner function")

    inner()
    inner()

outer1()

def outer():
    print("Outer function")

    def inner():
        print("Inner function")

    return 100

#if call outer() only it'll come like ans;outer function
value= outer()
print(value) #outer function #100


def outer():
    print("Outer function")

    def inner():
        print("Inner function")
    return inner

result=outer()
#print(result)
result()