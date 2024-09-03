#Return the function ref

def outer():
    print("Good Morning")

    def inner():
        print("Good Afternoon")

    return inner  

a= outer()
a()
