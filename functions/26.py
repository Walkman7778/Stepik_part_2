# task in russian here --- https://stepik.org/lesson/512854/step/16?unit=505068
# here is realized Gorner algorithm which work as recursion
# the list coefficient contain coefficients of polynomial and x is the argument of polynomial 

coefficient = input().split()
x = int(input())
def evaluate(coefficient, x):
    result = int(coefficient[0])
    for i in range(len(coefficient) - 1):
        result = result * x + int(coefficient[i + 1])
    return result 
print(evaluate(coefficient, x))