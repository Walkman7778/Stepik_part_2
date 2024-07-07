# task here --- https://stepik.org/lesson/446698/step/12?unit=437004
words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

result = {i: [ord(j) for j in i] for i in words}
