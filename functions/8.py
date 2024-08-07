# task in russian here --- https://stepik.org/lesson/508939/step/13?unit=501049
# I must sort the list of tuples by key equal input one of 4 variants from 1 to 4 corresponding to the element of tuple
# in cycle for we print the result , unpacking tuples
athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
num = int(input())
def sorts(el):
    return el[num -1]
for i in (sorted(athletes, key=sorts)):
    print(*i)