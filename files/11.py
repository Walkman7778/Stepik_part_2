# task in russian here --- https://stepik.org/lesson/530408/step/11?unit=523223
import re
with open(r'nums.txt', encoding='utf-8') as file:
    s = [re.findall(r'\d+', line) for line in file.readlines()]
    print(sum([sum([int(z) for z in i]) for i in s]))