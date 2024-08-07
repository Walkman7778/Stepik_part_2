# task here --- https://stepik.org/lesson/356379/step/14?unit=340494
import random
s = []
for _ in range(7):
    num = random.randrange(1, 49)
    s.append(num)
s = sorted(s)
print(*s, sep=" ")