# task here --- https://stepik.org/lesson/488831/step/7?unit=480067
#
a = input()
a1 = ""
s = list(a)
# initializing a dictionary with keys as order of sign in str- a and value its value
dict1 = dict(zip(list(range(len(s))), s))
dict2 = {}
# here  I use n and b sometimes , so I can t use function input() more than 1 time  
n = int(input())
b = [input().split(": ") for _ in range(n)]
# here I zip a dictionary with numbers as keys and letters as values
dict2 = dict(zip([int(i[1]) for i in b], [i[0] for i in b]))
# the main action forming a new str where I add to the a1 every sign from dictionary.values whose frequency 
# correspond to frequency to the sign i in s
for i in s:
    for key, value in dict2.items():
        if s.count(i) == key:
            a1 += value
print(a1)

