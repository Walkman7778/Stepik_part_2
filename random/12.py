# task here --- https://stepik.org/lesson/356380/step/13?thread=solutions&unit=340495
def generate_password(length):
    import random
    import string
    z =  [i for i in (string.ascii_letters + string.digits) if i not in 'l10IOo0']
    str1 = ""


    for _ in range(length):
        num = random.choice(z)
        str1 += num
    return str1
n, m = int(input()), int(input())
for _ in range(n):
    print(generate_password(m))


