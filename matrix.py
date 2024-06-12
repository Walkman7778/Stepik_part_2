n = int(input())
str1 = []
for i in range(n):
    str1.append(input().split())
summa1 = 0
summa2 = 0
summa3 = 0
summa4 = 0
for k in range(n):
    for j in range(n):
        if ((k > j) and (k < n - 1 -j)):
            summa1 += int(str1[k][j])
        if ((k < j) and (k > n - 1 -j)):
            summa2 += int(str1[k][j])
        if ((k > j) and (k > n - 1 -j)):
            summa3 += int(str1[k][j])
        if ((k > j) and (k < n - 1 -j)):
            summa4 += int(str1[k][j])  
print('Верхняя четверть:', summa1)
print('Правая четверть:', summa2)
print('Нижняя четверть:', summa3)
print('Левая четверть:', summa4)