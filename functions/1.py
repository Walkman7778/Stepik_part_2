# function parameters 
#Примечание 1. Приведенный ниже код:
#должен выводить:
#[[0]]
#[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
#[[9, 9, 9, 9], [9, 9, 9, 9], [9, 9, 9, 9]] """
def matrix(*args):
    match args:
        case ():
            return [[0]]
        case (n,):
            return [[0 for _ in range(n)] for _ in range(n)]
        case (n, m):
            return [[0 for _ in range(m)] for _ in range(n)]
        case (n, m, value):
            return [[value for _ in range(m)] for _ in range(n)]
print(matrix())
print(matrix(3))
print(matrix(2, 5))    
print(matrix(3, 4, 9))