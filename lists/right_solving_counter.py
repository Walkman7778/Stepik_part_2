# task here --- https://stepik.org/lesson/445791/step/15?unit=436052
import math
n = int(input())
s = [input() for _ in range(n)]
s2 = [i.split(":") for i in s]
s1 = set()
for i in s:
    s1.add(i)
counterall = len(s)
counterright = 0
counterallright = sum(1 for i in s1 if ('Correct' in i))
counterright = sum(1 for i in s2 if (i[1] == ' Correct'))
if n > 0:
    d = math.ceil(100 / n * counterright) if ((100 / n * counterright) % 1 >= 0.5) else math.floor(100 / n *             counterright)
if counterright > 0:
    print(f"Верно решили {counterallright} учащихся")
    print(f"Из всех попыток {d}% верных")
else:
    print("Вы можете стать первым, кто решит эту задачу")