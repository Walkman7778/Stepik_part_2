# task here --- https://stepik.org/lesson/356380/step/6?unit=340495
import random
s = []
def generate_ip():
    str1 = ""
    for _ in range(4):
        num = random.randrange(0, 255)
        s.append(num)
        str1 += f"{num}."
    return str1.rstrip(".")
print(generate_ip())