# task in russian here --- https://stepik.org/lesson/530408/step/10?unit=523223
with open(r'numbers.txt', encoding='utf-8') as file:
    s = file.readlines()
    s = [(i.rstrip()).split() for i in s ]
    for i in s:
        print(sum([int(z) for z in i]))