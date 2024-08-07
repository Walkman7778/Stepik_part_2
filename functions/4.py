# task in russian here --- https://stepik.org/lesson/503036/step/14?unit=494742
# the function get variable amount of incoming arguments 
# if argument type is str , we are returning it in view - number of incoming in arguments list -a , corresponding argument
# in format of string - b :
#'''   a) b   '''
# if in list of incoming arguments there  are no string value , we output "('Нет продуктов')" 
def print_products(*kargs):
    b = [i for i in list(kargs) if type(i) == str and len(i) > 0]
    if len(b) > 0:
        for i in range(len(b)):
            print(f'{i + 1}) {b[i]}')
    else:
        print('Нет продуктов')