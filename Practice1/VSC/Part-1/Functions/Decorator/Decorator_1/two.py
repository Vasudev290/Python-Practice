#Decorator is a function,it takes function as argument and modify that function, return modify function

def page_check(func):  #Decorator is a function,it takes function as argument
    
    def inner(name,login):
        if login == False:
            print("Please try to login first") #modify that function,
        else:
            return func(name,login)

    return inner #return modify function

def home_page(name,login):
    print("Home page",name)

@page_check
def order_page(name,login):
    print("Order page",name)

@page_check
def payment_page(name,login):
    print("payment page",name)


home_page("rahul",True)
order_page("rahul",False)
payment_page("rahul",False)