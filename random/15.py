# task here --- https://stepik.org/lesson/499669/step/8?unit=491205
import random
from math import pi

n = 10**6       # количество испытаний
k = 0
s0 = 4
for _ in range(n):
    x = random.uniform(-1, 1)     # случайное число с плавающей точкой от 0 до 1
    y = random.uniform(-1, 1)     # случайное число с плавающей точкой от 0 до 1

    if (x ** 2 + y ** 2 <= 1):                # если попадает в нужную область
        k += 1

print((k/n)*s0)