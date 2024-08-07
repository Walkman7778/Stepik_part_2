# task here --- https://stepik.org/lesson/362369/step/13?unit=346925
from fractions import Fraction as F
import itertools
sp = []
a = int(input())
for i, j in itertools.product(range(1, a + 1), range(1, a + 1)):
    if (F(i,j)) < 1 and (F(i,j)) not in sp :
        sp.append(F(i,j))

for i in sorted(sp):
    print(i)