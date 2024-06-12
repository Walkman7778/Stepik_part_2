numbers = ((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4), (90, 10))
string1 = list(numbers)
string2 = []
for i in numbers:
    sum = 0
    for j in i:
        sum += j
    string2.append(sum / len(i))
print(string2)