#recursive function
#Recursive functions are functions that calls itself.

def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)

    return result

result = factorial(6)
print(result)