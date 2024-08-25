# task in russian here --- https://stepik.org/lesson/511854/step/14?unit=504046
# using functions any and all
# here is input a number of classes which contain a number of persons with marks from 1 to 5 
# if in one class exist at least one person with mark 5 it must take True value 
# also the final result must return YES if in all  classes exist peoples with mark 5 and NO otherwise
list1 = []
for _ in range(int(input())):
    list0 = []
    for _ in range(int(input())):
        list0.append(*list(map(lambda i: int(i) == 5, input().split()[1])))
    list1.append(any(list0))
result = all(list1)
print(('NO', 'YES')[result])