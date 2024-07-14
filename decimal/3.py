#task here --- https://stepik.org/lesson/360941/step/12?unit=345464
from decimal import *
num = input()
num1 = Decimal(num)
if round(num1, 0) == 0:
    print(0 + num1.as_tuple().digits[-1])
else:
    num1 = num1.as_tuple()
    print(num1.digits[0] + num1.digits[-1])