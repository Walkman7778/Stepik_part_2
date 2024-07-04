a = list(input())
s = list(a)
dict1 = dict(zip(list(range(len(a))), a))
dict2 = {}
n = int(input())
b = [input().split(": ") for _ in range(n)]
dict2 = dict(zip([i[1] for i in b], [i[0] for i in b]))
for key, value in dict1.items():
    if a.count(value) == int(dict2[key]):
        print(dict2[key])
print(dict1)
print(dict2)

