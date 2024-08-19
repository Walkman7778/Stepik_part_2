# task in russian here --- https://stepik.org/lesson/512854/step/7?unit=505068
# writing a function using syntax of anonymous function which get string argument and return True 
# if argument is not negative , otherwise returns False 
# Firstly I change first "." into ""
# than I use 3 conditions : 1 - upper argument of lambda function must be equal with lower,
# 2 - first sign in argument is not equal with '-' , 3 - number of points in argument must be lower than 1 
# after replacing x =  x.replace('.','',1)
def is_non_negative_num(x):
    x =  x.replace('.','',1)
    return bool(list(filter((lambda x: True if (x.count('.') < 1) and 
    (x[0] != '-') and (x == x.lower() and x == x.upper()) else False), [x])))
print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))