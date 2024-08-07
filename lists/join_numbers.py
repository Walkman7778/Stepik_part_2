#we input a set of numbers on 2 lines 
# s3 = numbers which income in both sets 
# sorting an out set
s1 = {int(i) for i in input().split()}
s2 = {int(i) for i in input().split()}
s3 = s1 & s2
print(*sorted(s3))