# task in russian here --- https://stepik.org/lesson/519125/step/14?unit=511574
file = open(r'numbers.txt', 'r')
content = file.readlines()
z = [i.rstrip() for i in content]
file.close()
print(sum([int(i) for i in z]))