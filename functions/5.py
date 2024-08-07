# task in russian here --- https://stepik.org/lesson/503036/step/15?unit=494742
# output the meanings of input arguments as type of sorted dictionary 
def info_kwargs(**kwargs):
    s = sorted(kwargs.items())
    for i in s:
        print(f'{i[0]}: {i[1]}')