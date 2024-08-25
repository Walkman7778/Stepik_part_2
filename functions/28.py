# task in russian here --- https://stepik.org/lesson/511854/step/10?unit=504046
# here we must control contain the sphere points or no. Generators abscissas , ordinates and applicates have the 
# same length and contain coordinates of points on axes x, y, and z. 
# we must control if all points belong to the sphere or not 
# was used function map , zip , all and lambda 
# function all return True if all meanings of expression are True and False otherwise
# function zip make parallel iteration for finding each point x, y, z 
# function map create generator of changed elements and lambda verify final condition for the sphere.
abscissas = map(float, input().split())
ordinates = map(float, input().split())
applicates = map(float, input().split())
print(all(list(map(lambda x: x[0] ** 2 +  x[1] ** 2 +  x[2] ** 2 <= 4, zip(abscissas, ordinates, applicates)))))