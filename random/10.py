# task here --- https://stepik.org/lesson/356380/step/11?unit=340495
import random
import numpy as np
n = 5
lensample = list(range(1, 75))
matrix = [[0]*n for _ in range(n)]
list1 = (random.sample(lensample, 25))
list1 = [list1[i:i + 5] for i in range(0, len(list1), 5)]
matrix = np.array(list1)
matrix[2][2] = 0
for i in range(n):
    for j in range(n):
        print(str(matrix[i][j]).ljust(3), end=" ")
    print()