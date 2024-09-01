# task in russian here --- https://stepik.org/lesson/519126/step/9?unit=511575
import random
with open(r'random.txt', 'w') as file:
    for _ in range(25):
        file.write(str(random.randint(111, 777)) + '\n')