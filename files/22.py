# task in russian here --- https://stepik.org/lesson/519126/step/14?unit=511575
from datetime import datetime
with open(r'output.txt', 'w', encoding='UTF-8') as file, open(r'logfile.txt', 'r', encoding='UTF-8') as file1:
    s = file1.readlines()
    s1 = []
    fmt = '%H:%M'
    for i in s:
        name = i.split(', ')[0]
        begin = i.split(', ')[1]
        end = i.strip().split(', ')[2]
        t1_dt, t2_dt = datetime.strptime(str(end), fmt), datetime.strptime(str(begin), fmt)
        s = (t1_dt - t2_dt).seconds
        type(s) == int
        if s >= 3600:
            s1.append(name)
        s2 = ''
        s2 = ('\n'.join(s1))
    file.write(s2)