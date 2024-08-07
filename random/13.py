# task here --- https://stepik.org/lesson/356380/step/14?thread=solutions&unit=340495
def generate_password(length):
    import random
    import string
    z =  [i for i in (string.ascii_letters + string.digits) if i not in 'l10IOo0']
    z1 = [i for i in string.ascii_lowercase if i not in 'l10IOo0']
    z2 = [i for i in string.ascii_uppercase if i not in 'l10IOo0']
    z3 = [i for i in string.digits if i not in 'l10IOo0']
    str1 = ""


    for i in range(length + 1):
        num = ''
        if i == 1:
            num = random.choice(z3)
        elif i == 2:
            num = random.choice(z2)
        elif i == 3:
            num = random.choice(z1)
        elif i > 3:
            num = random.choice(z)
        str1 += num
    return str1
n, m = int(input()), int(input())
for _ in range(n):
    print(generate_password(m))