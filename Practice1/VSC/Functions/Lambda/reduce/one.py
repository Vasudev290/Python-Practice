#Reduce - reduce sequnce of elementing into a single element.
#reduce(function, sequnece)
#reduce() - (function,sequnce)-  from function import functiontools 

from functools import reduce
marks=[35,36,37,38,39,40]

result=reduce(lambda a,b:a+b,marks)
print(result)

