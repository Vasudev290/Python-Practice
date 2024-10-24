'''
Advantage:
instance user
consice code
by using lambda, we can write short code, improving code readibility.
'''

#Normal function
def cal_age(year):
    return 2024 - year
print(cal_age(2001)) #23
#obj_name= lambda argument : experssion
#Lambda
cal_a=lambda year : 2024-year
print(cal_a(2001))
