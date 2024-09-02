#How to convert local variable as global
def fun1():
    global a
    a=100

def fun2():
    print(a)

fun1()
fun2()