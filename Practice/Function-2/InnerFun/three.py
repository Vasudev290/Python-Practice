#How to execute inner function, outside the function?
def outer():
    def inner():
        print('Inner function')
    return inner
    
result=outer()
result()
result()
result()




