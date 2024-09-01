# task in russian here --- https://stepik.org/lesson/519126/step/12?unit=511575
with open(r'answer.txt', 'w') as file, open(r'goats.txt', 'r') as file1:
    lines = file1.read()
    s = lines.find('GOATS\n') + 6
    s0 = [i for i in lines[8:lines.find('GOATS\n')].split('\n') if i != '']
    s1 = lines[(lines.find('GOATS\n') + 6):].split('\n')
    dict1 = dict()
    for i in s0:
        dict1[i] = 0
    for j in s1:
        for i in dict1:
            if i == j:
                dict1[i] = dict1.get(i, 0) + 1
    for i in dict1:
        if ((int(dict1[i] / sum(dict1.values()) * 100)) > 7):
            file.write(i + '\n')