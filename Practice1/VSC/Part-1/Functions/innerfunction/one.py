#Inner Function
#a function that's defined within another function. 

def outer():
    print("Outer Function")

    def inner():
        print("Inner Function")

    inner()
    inner()

outer()
'''
Outer Function
Inner Function
Inner Function
'''

def outer():
    print("Outer Function")

    def inner():
        print("Inner Function")

    inner() #working

    
outer()
#inner() nameerror we have to right the inner function in inside the outer


#how to execute inner function, outside the function ?
def outer():

    def inner():
        print("Inner Function")

    #return 100,200 #(100,200)
    #return 'Hello,Good Morning'
    return inner #inner function or called by reference (return)


result = outer() 
#print(result)
result()
result()
result()
result()