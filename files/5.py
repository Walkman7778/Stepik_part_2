# task in russian here --- https://stepik.org/lesson/519125/step/15?unit=511574
file = open(r'nums.txt', 'r')
content = file.readlines()
z = [i.split() for i in content] 
z1 = [i for i in z if i != []] 
file.close()
print(sum([int(*i) for i in z1]))