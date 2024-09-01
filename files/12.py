# task in russian here --- https://stepik.org/lesson/530408/step/12?unit=523223
from string import ascii_letters
with open(r'file.txt', encoding='utf-8') as file:
    s = file.read()
    file.close()
    print('Input file contains:')
    print(sum(el in ascii_letters for el in s), 'letters')
    print(len(s.split()), 'words')
    print(len(s.split('\n')), 'lines')