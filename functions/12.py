# task in russian here --- https://stepik.org/lesson/508556/step/10?unit=500674
# here  I  use  function  map for rounding float numbers from list  
# function map get function round as 1 argument and list as a second argument 
def map(round, numbers):
    return [round(item, 2) for item in numbers]

numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
print(*map(round, numbers), sep="\n")