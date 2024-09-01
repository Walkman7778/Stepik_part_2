# task in russian here --- https://stepik.org/lesson/519125/step/13?unit=511574
import random
file = open(r'lines.txt', 'r')
content = file.readlines()
z = [i.rstrip() for i in content]
s = random.randint(0, len(content) - 1)
file.close()
print(z[s])