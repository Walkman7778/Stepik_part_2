# task in russian here --- https://stepik.org/lesson/508939/step/15?unit=501049
# I  must sort an input list of numbers split with ' ' by the sum of every numbers digits 
# for example this list ---  12 14 79 7 4 123 45 90 111 --- 
# will be sorted as --- 12 111 4 14 123 7 45 90 79 --- 
# here I used lambda function for reducing code 
list1 = input().split()
def functsort(list1):
    return sorted(list1, key=lambda x: sum(int(i) for i in str(x)))
print(*functsort(list1))