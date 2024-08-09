# task in russian here --- https://stepik.org/lesson/508939/step/14?unit=501049
# I must use a function - 1 of 5 without using "if"
import math
def квадрат(x):
    return (x ** 2)
def куб(x):
    return (x ** 3)
def корень(x):
    return(x ** 0.5)
def модуль(x):
    return abs (x)
def синус(x):
    return (math.sin(x))
reqfunction = {'квадрат': квадрат, 'куб': куб, 'корень': корень, 'модуль': модуль, 'синус': синус}
# here we input an argument for function 
number = int(input())
#here we input 1 from 5 permissed functions by the condition 
f1 = input()
print(reqfunction[f1](number))