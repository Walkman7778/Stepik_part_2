# task in russian here --- https://stepik.org/lesson/530408/step/9?unit=523223
with open(r'lines.txt', encoding='utf-8') as file:
    s = file.readlines()
    s = [i.rstrip() for i in s ]
    for i in s:
        if len(i) == len(max(s, key=len)):
            print(i)