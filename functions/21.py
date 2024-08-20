# task in russian here --- https://stepik.org/lesson/512854/step/10?unit=505068
# I must wrote a program which sort a list so :
# we must delete odd elements more then 47 and to devise each even element of created new list on 2 (x // 2)
# here I used 3 functions filter , map and lambda with conditions .
z = (list(filter(lambda x: (int(x) % 2 == 1 and x > 47), numbers)))
result1 = [i for i in numbers if i not in z]
print(*list(map(lambda x: (x // 2) if x % 2 == 0 else x, result1)))