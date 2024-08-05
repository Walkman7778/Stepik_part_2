# task here --- https://stepik.org/lesson/503036/step/13?unit=494742
# output the arguments of function as result , not researching how many arguments get function 
# first argument is positional, conserning to the condition 
def greet(name, *kargs):
    if len(kargs) == 0:
        return(f"Hello, {''.join(name)}!")
    elif len(kargs) == 1:
        return(f"Hello, {''.join(name)} and {''.join(kargs)}!")
    else:
        return(f"Hello, {name + ' and ' + ' and '.join(kargs)}!")