# task here --- https://stepik.org/lesson/362369/step/11?unit=346925
from fractions import Fraction
from math import factorial
n = input()
s = Fraction(sum(Fraction(1, factorial(i)) for i in range(1, int(n) + 1)))
print(s)
