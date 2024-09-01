# task in russian here --- https://stepik.org/lesson/519126/step/13?unit=511575
n = int(input())

content = ''
for i in range(n):
    with open(input(), 'r', encoding='utf-8') as r_file:
        content += r_file.read()
    
with open(r'output.txt', 'w') as file:
    file.write(content)