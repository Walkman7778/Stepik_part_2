# task in russian here --- https://stepik.org/lesson/530408/step/15?unit=523223
def read_csv():
    with open(r'data.csv', encoding='utf-8') as file:
        s = [i.rstrip().split(',') for i in file.readlines()]
        file.close()
        keys = s[0]
        values = s[1:]
    dict1 = [dict(zip(keys, i)) for i in values]
    return dict1