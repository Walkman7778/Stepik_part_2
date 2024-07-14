# task here --- https://stepik.org/lesson/362369/step/9?unit=346925
from fractions import Fraction
from decimal import Decimal

num1 = input()
num2 = input()

print(f'{num1} + {num2} = {Fraction(num1) + Fraction(num2)}')
print(f'{num1} - {num2} = {Fraction(num1) - Fraction(num2)}')
print(f'{num1} * {num2} = {Fraction(num1) * Fraction(num2)}')
print(f'{num1} / {num2} = {Fraction(num1) / Fraction(num2)}')