# first coommit while changing repo
numbers = (2, 3, 5, 7, -11, 13, 17, 19, 23, 29, 31, -6, 41, 43, 47, 53, 59, 61, -96, 71, 1000, -1)
str1 = list(numbers)
count = 1
for i in range(len(str1)):
    count *= int(str1[i])
print(count)