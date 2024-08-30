#Inner function - Inside a function ,we write one more function it's called inner function
def outer():
    print('Outer Function')

    def inner():
        print('Inner function')
    
    inner()
    inner()
    
outer()