#Map (Function, Sequnces)
#Filter (Function, Sequnces)


#Normal Function
mark= [34,35,36,37,38,39]
def add(mark):
    return mark + 1

a= map(add,mark)

print(list(a))

#Lambda Function
marks= [34,35,36,37,38,39,40]
Result = map(lambda marks:marks+1, marks)
print(list(Result))


