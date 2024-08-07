# task here --- https://stepik.org/lesson/356379/step/11?unit=340494
import random   
s = ["Орел", "Решка"]
n = int(input())
for _ in range(n):
  num = random.randrange(0,1)
  print(s[num])