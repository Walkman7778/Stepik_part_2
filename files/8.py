# task in russian here --- https://stepik.org/lesson/530408/step/8?unit=523223
with open(r'data.txt', encoding='utf-8') as file:
    s = file.readlines()[::-1]
    s = [i.strip('\n') for i in s] 
    print('\n'.join(s))