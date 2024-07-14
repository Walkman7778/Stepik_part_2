# task here --- https://stepik.org/lesson/360941/step/13?unit=345464
from decimal import Decimal
import math
d = Decimal(input())
d1 = Decimal(d.ln())
print(d.exp() + d.ln() + d.log10() + d.sqrt())