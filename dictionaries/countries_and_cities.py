# task in russian here """https://stepik.org/lesson/488831/step/5?unit=480067"""
dict1 = {}
countries = []
cities2 = []
for i in range(int(input())):
    countries.append(input().split())
for j in range(int(input())):
    cities2.append(input())
for i in range(len(cities2)):
    for j in countries:
        if cities2[i] in j:
            dict1[i] = dict1.get(i, j[0])
for i, j in dict1.items():
    print(j)