# task in russian here --- https://stepik.org/lesson/508939/step/12?unit=501049
# here I have a list of tuples - I must sort this list , by key -
# (min + max) value of each tuple value
numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
def comparator(i):
    x = min(list(i))
    y = max(list(i))
    return (x + y)
    
points = (sorted(numbers, key=comparator))
print(points)