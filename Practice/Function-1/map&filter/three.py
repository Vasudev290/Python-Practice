#filter(function, sequnces)
#Function
product_price=[1000,20,30,40,30,330,49,400,600,76]  #filter data based on conditions
new_Price= []
for price in product_price:
    if price<1000:
        new_Price.append(price)

print(new_Price)

#Lambda
product_price=[1000,20,30,40,30,330,49,400,600,76,34556]
filter_obj=filter(lambda product_price:product_price<=1000, product_price)
print(list(filter_obj))


""" filter_obj =filter(lambda product_pri:product_pri + 1, product_price)
neewproduct= list(filter_obj)
print(neewproduct)
 """
#filter
product_price=[1000,20,30,40,30,330,49,400,600,76]
def filterdata(price):
    return price<1000
newPrice=list(filter(filterdata,product_price))
print(product_price)
print(newPrice)
