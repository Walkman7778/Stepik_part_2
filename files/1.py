# task in russian here --- https://stepik.org/lesson/519125/step/11?unit=511574
# simple crunching the content of file 
file_name = input()
file = open(file_name, 'r')
content = file.read()
print(content)
file.close()