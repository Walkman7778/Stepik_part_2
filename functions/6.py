# task in russian here --- https://stepik.org/lesson/508939/step/11?unit=501049
# here I have a list of tuples -  they mean points on the coordinates system , and I must sort this list , by key -
# AB = ((x ** 2 + y ** 2) ** 0.5) the distance from the point on the system to the beginning of the coordinates system
points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
def comparator(i):
    x = i[0]
    y = i[1]
    return ((x ** 2 + y ** 2) ** 0.5)
    
points = (sorted(points, key=comparator))
print(points)