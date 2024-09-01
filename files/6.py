# task in russian here --- https://stepik.org/lesson/519125/step/16?unit=511574
file = open(r'prices.txt', 'r', encoding='utf-8')
content = file.readlines()
z1 = [i.split() for i in content]
z2 = [int(i[1]) * int(i[2]) for i in z1]
file.close()
print(sum(z2))