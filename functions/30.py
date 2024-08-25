# task in russian here --- https://stepik.org/lesson/511854/step/12?thread=solutions&unit=504046
# in the list of numbers from a to b must remain  only those which could be divided by each digit of respective 
# number
a, b = int(input()), int(input())
every_numb_div = [x for x in list(range(a, b + 1)) if ('0' not in str(x))]
print(*[i for i in every_numb_div if all(i % int(x) == 0 for x in str(i))])