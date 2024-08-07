# task here --- https://stepik.org/lesson/503036/step/12?unit=494742
# unpacking arguments in function m at least 2 meanings
def mean(*args):
    s, c = 0, 0
    for i in args:
        if type(i) == int or type(i) == float:
            s += i
            c += 1
    if c == 0:
        return 0.0
    else:
        return s / c