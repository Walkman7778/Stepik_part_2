# task here --- https://stepik.org/lesson/356379/step/12?unit=340494
import random

n = int(input())    # количество попыток

s = ["1", "2", "3", "4", "5", "6"]

for _ in range(n):
  num = random.randrange(0,5)
  print(s[num])