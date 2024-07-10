# task here --- https://stepik.org/lesson/356380/step/10?unit=340495
import random 
word = input()

s = []
for i in word:
    s.append(i)
c = random.sample(s, len(s))
str2 = ""
for i in c:
    str2 += i
print(str2)