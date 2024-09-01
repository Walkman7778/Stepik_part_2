# task in russian here --- https://stepik.org/lesson/530408/step/13?unit=523223
import random
with open(r'first_names.txt', encoding='utf-8') as file, open(r'last_names.txt', encoding='utf-8') as file2:
    s = file.read().split('\n')
    s2 = file2.read().split('\n')
    file.close()
    file2.close()
    c = (random.sample(s, 3))
    c2 = (random.sample(s2, 3))
    for i in list(zip(c, c2)):
        print(*i)