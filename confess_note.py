#first input number is number of students in the group
#than I input a list composed from family name and mark
#than another cicle for outputing the group 
# and condition of outputing the best students , who got the mark 4 or 5 in 5.point marking sistem
s = []
for i in range(int(input())):
    s.append(input().split())
for i in s:
    print(*i)
print()
for i in range(len(s)):
    if int(str(s[i][1])) >= 4:
        print(*s[i])