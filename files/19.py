# task in russian here --- https://stepik.org/lesson/519126/step/11?unit=511575
with open(r'new_scores.txt', 'w') as file, open(r'class_scores.txt', 'r') as file1:
    lines = file1.readlines()
    for i in lines:
        if (int(i.split()[1]) < 96):
            file.write(f'{i.split()[0]} {str(int(i.split()[1]) + 5)}\n')
        else:
            file.write(f'{i.split()[0]} {str(100)}\n')