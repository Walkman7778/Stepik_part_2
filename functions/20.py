# task in russian here --- https://stepik.org/lesson/512854/step/8?unit=505068
# the task is look like previous just without controlling by the negative 
# also was added  condition controlling the case "1-1" and ".-95" 
def is_num(x):
    if '.' in x[1:]:
        x =  x.replace('.','',1)
    else:
        x = x.replace('.','..',1)
    return bool(list(filter((lambda x: True if (x.count('.') < 1) and
                            (x.rfind('-') <= 0) and
                            (x == x.lower() and x == x.upper()) else False), [x])))
print(is_num('10.34ab'))
print(is_num('10.45'))
print(is_num('-18'))
print(is_num('-34.67'))
print(is_num('987'))
print(is_num('abcd'))
print(is_num('123.122.12'))
print(is_num('-123.122'))
print(is_num('--13.2'))