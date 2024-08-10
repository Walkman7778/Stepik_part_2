#task in russian here --- https://stepik.org/lesson/508556/step/11?unit=500674
# Here  I  with  function filter() and map() pick 
# from existing list numbers 3 digits - numbers % 5 == 2 
# and print their cubes, each on new line.
from math import fmod
def map(pow, items):
    return [pow(item, 3) for item in items]


def a_filter(x):
    if 99 < x < 1000:
        return x % 5 == 2

numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
numbers1 = map(pow, filter(a_filter, numbers))
for i in numbers1:
    print(i)