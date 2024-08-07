# task here --- https://stepik.org/lesson/362369/step/10?unit=346925 
from fractions import Fraction
from decimal import Decimal
n = input()
s = Fraction(sum(Fraction(1, (i ** 2)) for i in range(1, int(n) + 1)))
print(s)