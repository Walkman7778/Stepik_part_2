# task in russian here --- https://stepik.org/lesson/519126/step/10?unit=511575
with open(r'output.txt', 'w') as file, open(r'input.txt', 'r') as file1:
    lines = file1.readlines()
    for i in range(len(lines)):
        file.write(f'{i + 1}) {lines[i]}')