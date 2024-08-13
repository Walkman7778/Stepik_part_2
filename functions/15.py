# task in russian here --- https://stepik.org/lesson/508556/step/14?unit=500674
# writing a function which have as an argument another function for example functions 
#---------def add3(x):
#---------    return x + 3
#
#---------def mul7(x):
#---------    return x * 7
#---------print(func_apply(mul7, [1, 2, 3, 4, 5, 6]))
#---------print(func_apply(add3, [1, 2, 3, 4, 5, 6]))
#---------print(func_apply(str, [1, 2, 3, 4, 5, 6]))
#   must return 
#   [7, 14, 21, 28, 35, 42]
#   [4, 5, 6, 7, 8, 9]
#   ['1', '2', '3', '4', '5', '6']


def func_apply(function, items):
    new_list = []
    for item in items:
        new_item = function(item)
        new_list.append(new_item)
    return s
