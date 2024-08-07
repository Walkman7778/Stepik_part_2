s = input().split()
arr = []
d = dict()
for el in s:
    if el not in arr:
        arr.append(el)
    else:
        d[el] = d.get(el,0) + 1
        arr.append(f'{el}_{str(d[el])}')
        
print(*arr)