# task here --- https://stepik.org/lesson/446698/step/10?unit=437004
s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 54:car 3:island 88:power 7:box 17:star 101:ice'

result = {int(i[0]): i[1] for i in [j.split(':') for j in list(s.split())]}
