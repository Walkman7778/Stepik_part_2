#for function ax ** 2 + bx + c
a, b, c = int(input()), int(input()), int(input())
str1 = [-b/(2 * a), (4 * a * c - (b ** 2) )/ (4 * a)]
print(tuple(str1))