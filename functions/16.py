# task in russian here --- https://stepik.org/lesson/503099/step/15?unit=494805
from functools import reduce

floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59, 34.23, 12.12, 4.67, 2.45, 9.32]
words = ['racecar', 'akinremi', 'deed', 'temidayo', 'omoseun', 'civic', 'TATTARRATTAT', 'malayalam', 'nun']
numbers = [4, 6, 9, 23, 5]
# this function works better in Trinket
def filter_map(num):
    return round((num**2), 1)
# this function also 
def filter_for_lambda(name):
    return (len(name) > 4 and name == name[::-1])

# first function map get as argument function lambda , filter function filter map and initial list 
# but it returns a generator and for output correct result I use list(map(...))
map_result = list(map(lambda num: filter_map(num), floats))
# tse same as in previous function
filter_result = list(filter(lambda name: filter_for_lambda(name), words))
# here function reduce get as initial argument first element from list numbers 
reduce_result = reduce(lambda num1, num2: num1 * num2, numbers)

print([i for i in map_result])
print(filter_result)
print(reduce_result)