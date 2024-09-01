# task in russian here --- https://stepik.org/lesson/519125/step/12?unit=511574
file_name = input()
file = open(file_name, 'r')
content = file.readlines()
print(content[-2])
file.close()