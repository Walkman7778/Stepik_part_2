#task in russian here --- https://stepik.org/lesson/508939/step/16?unit=501049
# the same as the previous sample ,  only the  sorting is doing by non decreasing numbers from list 
list1 = sorted([int(i) for i in input().split()])
def functsort(list1):
    return sorted(list1,key=lambda x: sum(int(i) for i in str(x)))
print(*functsort(list1))