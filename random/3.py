# task here --- https://stepik.org/lesson/356379/step/13?unit=340494
import random

length = int(input())
for _ in range(length):
  num = (random.randrange(65,90) or random.randrange(97,122))
  print(chr(num), end="")