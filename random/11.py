# secret friend
# task here --- https://stepik.org/lesson/356380/step/12?unit=340495
# without random
n = int(input())
s = [input() for _ in range(n)]
s2 = []
for i in range(len(s)):
    if (i + 1) < len(s):
        s2.append(f"{s[i]} - {s[i + 1]}")
    elif i == len(s):
        s2.append(f"{s[i]} - {s[0]}")
print(s2)