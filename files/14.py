# task in russian here --- https://stepik.org/lesson/530408/step/14?unit=523223
with open(r'population.txt', encoding='utf-8') as file:
    s = file.readlines()
    file.close()
    s1 = [i.rstrip().split('\t') for i in s]
    for i in s1:
        if (i[0][0] == 'G') and (int(i[-1]) > 500_000):
            print(i[0])