# task in russian here --- https://stepik.org/lesson/530408/step/7?unit=523223
with open(r'text.txt', encoding='utf-8') as file:
    print(file.readline().strip()[::-1])